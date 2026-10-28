#!/usr/bin/env python3
"""In The Loop · ferramenta do deck.

O deck é um arquivo-fonte `.itl.html`: um comentário de cabeçalho e uma sequência de
<section class="itl" ...> compostas só com as classes itl-* e os tokens do design system.

  <!-- itl:deck titulo="In The Loop · Q4 2026" ano="2026" -->            (deck montado)
  <!-- itl:parte bloco="Squad Alfa" apresentador="Nome" cargo="Cargo" edicao="2026-Q4" -->   (parte de um apresentador)
  <section class="itl"> ... <aside class="itl-notas">…</aside></section>

Comandos
  itl.py verificar  ARQ.itl.html            regras do design system (classes, tokens, imagens, notas) + avisos de texto longo
  itl.py gerar      ARQ.itl.html -o SAIDA   HTML único, autocontido (fontes, imagens WebP, motor); roda `verificar` antes
  itl.py pendencias ARQ.itl.html            lista PENDENTE:, PARA O DESIGN: e imagens pedidas (com a foto de referência)
  itl.py pacote     PARTE.itl.html --versao N -o PASTA
                                            o que vai para o Slack: prévia .html, fonte .zip (com img/), pendências .md, entrega.json
  itl.py montar     PARTES... -o DECK.itl.html --trimestre Q4 --mes Janeiro --ano 2027
                                            junta as partes no deck final (capa e agenda geradas; aberturas numeradas pelo motor)
  itl.py componentes                        regenera COMPONENTES.md a partir dos comentários @componente do CSS

A verificação visual (texto cabendo no container) roda no navegador: tecla V no deck gerado,
ou ITL.verificar() no console.
"""
import argparse, base64, datetime, hashlib, html, io, json, os, re, shutil, sys, tempfile, unicodedata, zipfile
from html.parser import HTMLParser

SLIDES = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))   # a skill é autocontida
ASSETS = os.path.join(SLIDES, 'assets')
CSS = os.path.join(SLIDES, 'design-system.css')

# limites de texto (avisos, não erros): empurram o conteúdo para o que cabe no telão
LIMITE_TITULO = {'g': 30, 'm': 80, '': 70}
LIMITES = {'itl-gigante': 16, 'itl-palavra': 12, 'itl-sub': 80, 'itl-texto': 260, 'itl-frase': 100,
           'itl-kicker': 40, 'itl-cap': 60, 'itl-premio': 16}
VOID = {'img', 'br', 'hr', 'meta', 'link', 'input', 'source', 'wbr'}
MODIFICADORES = {'g', 'm', 'centro', 'base', 'fim', 'meio', 'destaque', 'branco', 'meta', 'rolagem'}
PROPS_LIVRES = {'grid-column', 'grid-row', 'align-self', 'justify-self', 'order', 'flex', 'width', 'max-width',
                'height', 'min-height', 'text-align', 'gap', 'margin-top', 'align-items', 'justify-content'}
TOKENS_LIVRES = {'n', 'v', 'div', 'foco', 'zoom'}
PROIBIDO_VALOR = re.compile(r'#|rgb|hsl|url\(|font|!important|expression', re.I)
TAGS_PROIBIDAS = {'script', 'style', 'link', 'iframe', 'object', 'embed', 'font', 'meta', 'base'}


def versao_css():
    m = re.search(r'design system v(\d+\.\d+\.\d+)', open(CSS, encoding='utf-8').read())
    return m.group(1) if m else '0.0.0'


def classes_css():
    return set(re.findall(r'\.(itl-[a-z0-9-]+)', open(CSS, encoding='utf-8').read()))


def tokens():
    return set(re.findall(r'--([a-z0-9-]+)\s*:', open(CSS, encoding='utf-8').read()))


def slug(txt):
    t = unicodedata.normalize('NFKD', txt or '').encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-') or 'bloco'


# ---------------------------------------------------------------- leitura
def ler(caminho):
    fonte = open(caminho, encoding='utf-8').read()
    m = re.search(r'<!--\s*itl:(deck|parte)(.*?)-->', fonte, re.S)
    meta = {k: html.unescape(v) for k, v in re.findall(r'(\w+)="([^"]*)"', m.group(2))} if m else {}
    meta['_tipo'] = m.group(1) if m else ''
    return fonte, meta


class Leitor(HTMLParser):
    def __init__(self, validas, toks):
        super().__init__(convert_charrefs=True)
        self.validas, self.toks = validas, toks
        self.erros, self.avisos, self.imgs, self.secoes = [], [], [], []
        self.slide = 0
        self.pilha = []      # elementos com limite de texto: [tag, limite, nome, texto]
        self.contexto = []   # classes dos elementos abertos

    def onde(self):
        return 'slide %d (linha %d)' % (self.slide, self.getpos()[0])

    def limite_de(self, tag, cls):
        if 'itl-titulo' in cls:
            mod = next((m for m in ('g', 'm') if m in cls), '')
            return LIMITE_TITULO[mod], 'título' + (' (%s)' % mod if mod else '')
        for c in LIMITES:
            if c in cls:
                return LIMITES[c], c
        anc = [c for lista in self.contexto for c in lista]
        if tag == 'h3' and 'itl-topico' in anc:
            return 40, 'título de tópico'
        if tag == 'p' and ('itl-topico' in anc or 'itl-metrica' in anc):
            return 140, 'texto de tópico/métrica'
        if tag == 'li' and 'itl-lista' in anc:
            return 70, 'item de lista'
        if tag == 'b' and 'itl-agenda' in anc:
            return 24, 'item da agenda'
        return None, None

    def handle_data(self, data):
        for e in self.pilha:
            e[3] += data

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.contexto:
            self.contexto.pop()
        for i in range(len(self.pilha) - 1, -1, -1):
            if self.pilha[i][0] == tag:
                _, lim, nome, texto = self.pilha.pop(i)
                n = len(' '.join(texto.split()))
                if n > lim:
                    self.avisos.append('slide %d: texto longo (%d > %d) em %s: «%s…»' % (self.slide, n, lim, nome, ' '.join(texto.split())[:40]))
                break

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get('class') or '').split()
        if tag not in VOID:
            self.contexto.append(cls)
            lim, nome = self.limite_de(tag, cls)
            if lim:
                self.pilha.append([tag, lim, nome, ''])
        if tag == 'section':
            self.slide += 1
            if 'itl' not in cls:
                self.erros.append('%s: <section> precisa de class="itl"' % self.onde())
            self.secoes.append({'slide': self.slide, 'notas': False, 'agenda': a.get('data-agenda')})
        if tag in TAGS_PROIBIDAS:
            self.erros.append('%s: <%s> não é permitido no conteúdo' % (self.onde(), tag))
        for k, v in attrs:
            if k.startswith('on'):
                self.erros.append('%s: atributo %s não é permitido' % (self.onde(), k))
            if k == 'class':
                for c in (v or '').split():
                    if c == 'itl' and tag == 'section':
                        continue
                    if c.startswith('itl-'):
                        if c not in self.validas:
                            self.erros.append('%s: classe "%s" não existe no design system' % (self.onde(), c))
                    elif c not in MODIFICADORES:
                        self.erros.append('%s: classe "%s" fora do design system (use itl-* ou modificadores documentados)' % (self.onde(), c))
                    if c == 'itl-notas' and self.secoes:
                        self.secoes[-1]['notas'] = True
            if k == 'style' and v:
                for decl in [d.strip() for d in v.split(';') if d.strip()]:
                    if ':' not in decl:
                        continue
                    p, val = [x.strip() for x in decl.split(':', 1)]
                    if PROIBIDO_VALOR.search(val):
                        self.erros.append('%s: style "%s" — cor e fonte só pelo design system' % (self.onde(), decl))
                    elif p.startswith('--'):
                        if p[2:] not in TOKENS_LIVRES:
                            self.erros.append('%s: variável %s não é ajustável no slide (use %s)' % (self.onde(), p, ', '.join('--' + t for t in sorted(TOKENS_LIVRES))))
                        for t in re.findall(r'var\(--([a-z0-9-]+)\)', val):
                            if t not in self.toks:
                                self.erros.append('%s: token --%s não existe' % (self.onde(), t))
                        if not re.fullmatch(r'(var\(--[a-z0-9-]+\)|-?[\d.]+(px|%|em)?|\s)+', val):
                            self.erros.append('%s: valor "%s" em %s — use token ou número' % (self.onde(), val, p))
                    elif p not in PROPS_LIVRES:
                        self.erros.append('%s: propriedade "%s" não é permitida em style (só layout: %s)' % (self.onde(), p, ', '.join(sorted(PROPS_LIVRES))))
        if tag == 'img':
            src = a.get('src', '')
            if not src:
                self.erros.append('%s: <img> sem src (para imagem que falta, use <div data-pedido="...">)' % self.onde())
            elif re.match(r'https?:', src):
                self.erros.append('%s: imagem externa (%s) — salve o arquivo junto do deck, em img/' % (self.onde(), src))
            else:
                self.imgs.append((self.slide, src))
            if 'alt' not in a:
                self.avisos.append('%s: <img> sem alt' % self.onde())
        if a.get('data-referencia'):
            self.imgs.append((self.slide, a['data-referencia']))
        if 'data-de' in a and not re.fullmatch(r'\d{1,2}', a['data-de'] or ''):
            self.avisos.append('%s: data-de="%s" — o odômetro só roda com inteiro de até 2 dígitos' % (self.onde(), a['data-de']))


def verificar(caminho, silencioso=False):
    fonte, meta = ler(caminho)
    base = os.path.dirname(os.path.abspath(caminho))
    L = Leitor(classes_css(), tokens())
    L.feed(fonte)
    if not meta['_tipo']:
        L.avisos.append('sem cabeçalho <!-- itl:parte bloco="…" apresentador="…" cargo="…" --> nem <!-- itl:deck … -->')
    for slide, src in L.imgs:
        if not src.startswith('data:') and not os.path.exists(os.path.join(base, src)):
            L.erros.append('slide %d: imagem não encontrada: %s' % (slide, src))
    for s in L.secoes:
        if not s['notas']:
            L.avisos.append('slide %d: sem notas do apresentador (<aside class="itl-notas">)' % s['slide'])
    if re.search(r'lorem ipsum', fonte, re.I):
        L.erros.append('o arquivo contém "lorem ipsum" — troque por conteúdo real ou PENDENTE:')
    if not silencioso:
        for e in L.erros:
            print('ERRO  ', e)
        for w in L.avisos:
            print('aviso ', w)
        print('%d slide(s) · %d erro(s) · %d aviso(s) · design system v%s' % (len(L.secoes), len(L.erros), len(L.avisos), versao_css()))
    return L


# ---------------------------------------------------------------- geração
def data_uri(caminho, mime):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(caminho, 'rb').read()).decode())


def fontes():
    f = lambda n: data_uri(os.path.join(ASSETS, 'fontes', n), 'font/woff2')
    return '\n'.join([
        "@font-face{font-family:'DM Mono';font-weight:400;font-display:block;src:url(%s) format('woff2')}" % f('dmmono-400.woff2'),
        "@font-face{font-family:'DM Mono';font-weight:500;font-display:block;src:url(%s) format('woff2')}" % f('dmmono-500.woff2'),
        # reserva com as mesmas medidas da Helvetica/Arial, para máquina sem Helvetica Neue
        "@font-face{font-family:'ITL Reserva';font-weight:400 700;font-display:block;src:url(%s) format('woff2')}" % f('arimo.woff2'),
    ])


def assets():
    g = lambda n: data_uri(os.path.join(ASSETS, 'glows', n), 'image/webp')
    l = lambda n: data_uri(os.path.join(ASSETS, 'logos', n), 'image/svg+xml')
    return {'shape': g('shape.webp'), 'anel': g('anel.webp'), 'infinito': g('infinito.webp'),
            'logoItl': l('in-the-loop.svg'), 'logoVolund': l('volund.svg')}


def webp(caminho, maximo=1920):
    try:
        from PIL import Image, ImageOps
    except ImportError:
        sys.exit('Falta a biblioteca Pillow (converte as imagens para WebP). Instale com: pip install pillow')
    if caminho.lower().endswith('.svg'):
        return data_uri(caminho, 'image/svg+xml')
    im = Image.open(caminho)
    if im.format == 'WEBP' and max(im.size) <= maximo:
        return data_uri(caminho, 'image/webp')
    im = ImageOps.exif_transpose(im)
    if im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGBA')
    im.thumbnail((maximo, maximo))
    buf = io.BytesIO()
    im.save(buf, 'WEBP', quality=82, method=5)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()


def gerar(caminho, saida):
    L = verificar(caminho)
    if L.erros:
        sys.exit('não gerado: corrija os erros acima.')
    fonte, meta = ler(caminho)
    base = os.path.dirname(os.path.abspath(caminho))
    imagens = {}

    def troca(m):
        src = m.group(2)
        if src.startswith('data:'):
            return m.group(0)
        p = os.path.join(base, src)
        k = hashlib.sha1(open(p, 'rb').read()).hexdigest()[:12]
        if k not in imagens:
            imagens[k] = webp(p)
        return '<img%sdata-src="%s"' % (m.group(1), k)

    slides = re.sub(r'<!--\s*itl:(deck|parte).*?-->', '', fonte, flags=re.S)
    slides = re.sub(r'<img\b([^>]*?)(?<![\w-])src="([^"]+)"', troca, slides)
    titulo = meta.get('titulo') or ('In The Loop · ' + meta['bloco'] if meta.get('bloco') else 'In The Loop')
    ano = meta.get('ano') or (meta.get('edicao', '')[:4] if re.match(r'\d{4}', meta.get('edicao', '')) else str(datetime.date.today().year))
    t = open(os.path.join(SLIDES, 'template.html'), encoding='utf-8').read()
    rep = {
        '/*ITL:TITULO*/': html.escape(titulo),
        '/*ITL:ANO*/': html.escape(ano),
        '/*ITL:VERSAO*/': versao_css(),
        '/*ITL:FONTES*/': fontes(),
        '/*ITL:CSS*/': open(CSS, encoding='utf-8').read(),
        '/*ITL:SLIDES*/': slides,
        '/*ITL:ASSETS*/{}': json.dumps(assets()),
        '/*ITL:IMAGENS*/': json.dumps(imagens),
        '/*ITL:MOTOR*/': open(os.path.join(SLIDES, 'motor.js'), encoding='utf-8').read(),
    }
    for k, v in rep.items():
        t = t.replace(k, v)
    open(saida, 'w', encoding='utf-8').write(t)
    print('ok %s · %d slide(s) · %d imagem(ns) · %.1f MB' % (saida, len(L.secoes), len(imagens), os.path.getsize(saida) / 1048576))


# ---------------------------------------------------------------- pendências
def listar_pendencias(caminho):
    fonte, _ = ler(caminho)
    saida, n = [], 0
    for p in re.split(r'(?=<section\b)', fonte):
        if not p.startswith('<section'):
            continue
        n += 1
        texto = re.sub(r'<[^>]+>', ' ', p)
        for m in re.finditer(r'(PENDENTE|PARA O DESIGN):\s*([^\n<]+)', texto):
            saida.append((n, m.group(1), m.group(2).strip(), None))
        for m in re.finditer(r'<[^>]*data-pedido="([^"]+)"[^>]*>', p):
            ref = re.search(r'data-referencia="([^"]+)"', m.group(0))
            saida.append((n, 'IMAGEM', html.unescape(m.group(1)), ref.group(1) if ref else None))
    return saida


def pendencias(caminho):
    itens = listar_pendencias(caminho)
    for n, tipo, txt, ref in itens:
        print('slide %2d · %s: %s%s' % (n, tipo, txt, ' (referência: %s)' % ref if ref else ''))
    print('%d pendência(s)' % len(itens))


# ---------------------------------------------------------------- pacote para o Slack
def pacote(caminho, versao, saida, edicao=None):
    """Arquivos de uma entrega no Slack (o nome carrega ano, trimestre, bloco e versão):
       ITL-<edicao>-<bloco>-vN.html   prévia autocontida da parte (abre com duplo clique)
       ITL-<edicao>-<bloco>-vN.zip    fonte (parte.itl.html) + img/ (inclui as fotos de referência dos pedidos)
       pendencias-<bloco>-vN.md       PENDENTE / PARA O DESIGN / imagens pedidas
       entrega.json                   manifesto"""
    L = verificar(caminho)
    if L.erros:
        sys.exit('não empacotado: corrija os erros acima.')
    fonte, meta = ler(caminho)
    if meta['_tipo'] != 'parte':
        sys.exit('falta o cabeçalho <!-- itl:parte bloco="…" apresentador="…" cargo="…" edicao="2026-Q4" -->')
    edicao = edicao or meta.get('edicao')
    if not edicao or not re.fullmatch(r'\d{4}-Q[1-4]', edicao):
        sys.exit('informe a edição no formato 2026-Q4 (--edicao ou edicao="" no cabeçalho)')
    base = os.path.dirname(os.path.abspath(caminho))
    sl = slug(meta.get('bloco'))
    nome = 'ITL-%s-%s-v%d' % (edicao, sl, versao)
    os.makedirs(saida, exist_ok=True)

    usados, mapa = {}, {}
    def troca(mm):
        src = mm.group(3)
        if re.match(r'(https?:|data:)', src):
            return mm.group(0)
        origem = os.path.normpath(os.path.join(base, src))
        if origem not in mapa:
            arc = 'img/' + os.path.basename(origem)
            if arc in usados and usados[arc] != origem:
                arc = 'img/%s-%s' % (hashlib.sha1(origem.encode()).hexdigest()[:6], os.path.basename(origem))
            usados[arc] = origem
            mapa[origem] = arc
        return '%s%s="%s"' % (mm.group(1), mm.group(2), mapa[origem])
    fonte_pkg = re.sub(r'(\s)((?<![\w-])src|data-referencia)="([^"]+)"', troca, fonte)

    with zipfile.ZipFile(os.path.join(saida, nome + '.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('parte.itl.html', fonte_pkg)
        for arc, origem in usados.items():
            z.write(origem, arc)
    gerar(caminho, os.path.join(saida, nome + '.html'))

    itens = listar_pendencias(caminho)
    linhas = ['# Pendências · %s · v%d' % (meta.get('bloco', ''), versao), '']
    linhas += ['- slide %d · %s: %s%s' % (n, t, x, ' (referência: %s)' % mapa.get(os.path.normpath(os.path.join(base, r)), r) if r else '') for n, t, x, r in itens] or ['Nenhuma pendência.']
    open(os.path.join(saida, 'pendencias-%s-v%d.md' % (sl, versao)), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    manifesto = {'bloco': meta.get('bloco'), 'apresentador': meta.get('apresentador'), 'cargo': meta.get('cargo'), 'edicao': edicao,
                 'versao': versao, 'slides': len(L.secoes), 'imagens': len(usados),
                 'imagens_pedidas': sum(1 for i in itens if i[1] == 'IMAGEM'),
                 'pendentes': sum(1 for i in itens if i[1] == 'PENDENTE'),
                 'para_o_design': sum(1 for i in itens if i[1] == 'PARA O DESIGN'),
                 'design_system': versao_css(), 'gerado_em': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                 'arquivos': [nome + '.html', nome + '.zip', 'pendencias-%s-v%d.md' % (sl, versao)]}
    json.dump(manifesto, open(os.path.join(saida, 'entrega.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('ok pacote %s · v%d · %d slide(s) · %d imagem(ns) · %d pedida(s) · %d pendente(s) → %s'
          % (meta.get('bloco'), versao, len(L.secoes), len(usados), manifesto['imagens_pedidas'], manifesto['pendentes'], saida))


# ---------------------------------------------------------------- montagem (designer)
CAPA = """<section class="itl" data-limpo>
  <ul class="itl-capa"><li>%(linha1)s</li><li><b>%(trimestre)s</b> · %(mes)s · %(ano)s</li><li>%(polos)s</li></ul>
  <aside class="itl-notas">Tela de abertura. Fica no ar enquanto todos se acomodam.</aside>
</section>
"""


def ler_parte(caminho):
    fonte, meta = ler(caminho)
    if meta['_tipo'] != 'parte' or not meta.get('bloco'):
        sys.exit('%s: falta o cabeçalho <!-- itl:parte bloco="…" apresentador="…" cargo="…" -->' % caminho)
    corpo = re.sub(r'<!--\s*itl:parte.*?-->', '', fonte, flags=re.S).strip()
    return meta, corpo, os.path.dirname(os.path.abspath(caminho))


def agenda_html(partes):
    # só os blocos com abertura (data-agenda) entram; partes do design, como o cerimonial, ficam de fora
    itens = ''.join('\n      <li><b>%s</b><span>%s</span></li>' % (html.escape(m['bloco']), html.escape(m.get('apresentador', ''))) for m, c, _ in partes if 'data-agenda=' in c)
    return ('<section class="itl">\n  <div class="itl-area">\n    <p class="itl-kicker" data-a="surge">Agenda do dia</p>\n'
            '    <ol class="itl-agenda">%s\n    </ol>\n  </div>\n  <aside class="itl-notas">Agenda gerada a partir dos blocos do deck.</aside>\n</section>\n' % itens)


def montar(arquivos, saida, trimestre, mes, ano, linha1, polos, capa=True, agenda=True):
    partes = [ler_parte(a) for a in arquivos]
    pasta_saida = os.path.dirname(os.path.abspath(saida))
    out = ['<!-- itl:deck titulo="In The Loop · %s %s" ano="%s" -->' % (html.escape(trimestre), html.escape(ano), html.escape(ano)),
           '<!-- Deck montado por itl.py montar a partir de: %s -->' % ', '.join(os.path.basename(a) for a in arquivos), '']
    if capa:
        out.append(CAPA % {k: html.escape(v) for k, v in dict(linha1=linha1, trimestre=trimestre, mes=mes, ano=ano, polos=polos).items()})
    if agenda:
        if len(partes) > 8:
            print('aviso  mais de 8 blocos: agenda não gerada. Divida em duas à mão (PARA O DESIGN).')
        elif sum(1 for _, c, _ in partes if 'data-agenda=' in c) >= 2:
            out.append(agenda_html(partes))
    n = 0
    for meta, corpo, base in partes:
        def reescreve(m):
            src = m.group(3)
            if re.match(r'(https?:|data:)', src):
                return m.group(0)
            return '%s%s="%s"' % (m.group(1), m.group(2), os.path.relpath(os.path.realpath(os.path.join(base, src)), os.path.realpath(pasta_saida)))
        out.append('<!-- ===== %s%s ===== -->' % (meta['bloco'], ' · ' + meta['apresentador'] if meta.get('apresentador') else ''))
        out.append(re.sub(r'(\s)((?<![\w-])src|data-referencia)="([^"]+)"', reescreve, corpo) + '\n')
        n += corpo.count('<section')
    open(saida, 'w', encoding='utf-8').write('\n'.join(out))
    print('ok %s · %d bloco(s) · %d slide(s) de conteúdo' % (saida, len(partes), n))
    verificar(saida)


def componentes():
    css = open(CSS, encoding='utf-8').read()
    linhas = ['# Componentes do design system In The Loop', '',
              'Gerado por `itl.py componentes` a partir de `design-system.css` (v%s). Não editar à mão.' % versao_css(), '',
              '## Slide', '',
              '`<section class="itl">` · `data-limpo` (sem masthead, grade e paginação) · `data-agenda="Nome"`.', '',
              'Animação genérica: `data-a="sobe"` · `"surge"` · `"linhas"` (título por máscara de linha; `data-linhas="2"` limita as linhas). '
              'Números: `data-conta` conta até o valor; `data-de="4"` num `.itl-numero` inteiro de até 2 dígitos vira odômetro.', '',
              'Modificadores aceitos (sem prefixo): ' + ', '.join('`%s`' % m for m in sorted(MODIFICADORES)) + '.', '',
              'Em `style` só entram as variáveis ' + ', '.join('`--%s`' % t for t in sorted(TOKENS_LIVRES)) +
              ' (número ou token) e propriedades de layout: ' + ', '.join(sorted(PROPS_LIVRES)) + '.', '',
              'Imagem que ainda não existe: `<div data-pedido="o que é preciso" data-referencia="img/foto-enviada.jpg"></div>`.', '',
              '## Componentes', '']
    for m in re.finditer(r'/\*\s*@componente\s+(.*?)\*/', css, re.S):
        linhas.append('- ' + ' '.join(m.group(1).split()))
    open(os.path.join(SLIDES, 'COMPONENTES.md'), 'w', encoding='utf-8').write('\n'.join(linhas) + '\n')
    print('ok COMPONENTES.md')


def main():
    ap = argparse.ArgumentParser(description='In The Loop · ferramenta do deck')
    sub = ap.add_subparsers(dest='cmd', required=True)
    v = sub.add_parser('verificar'); v.add_argument('arquivo')
    g = sub.add_parser('gerar'); g.add_argument('arquivo'); g.add_argument('-o', '--saida', required=True)
    p = sub.add_parser('pendencias'); p.add_argument('arquivo')
    k = sub.add_parser('pacote'); k.add_argument('parte'); k.add_argument('--versao', type=int, required=True)
    k.add_argument('--edicao', help='ex.: 2026-Q4 (padrão: edicao="" do cabeçalho)'); k.add_argument('-o', '--saida', required=True)
    m = sub.add_parser('montar'); m.add_argument('partes', nargs='+'); m.add_argument('-o', '--saida', required=True)
    m.add_argument('--trimestre', required=True, help='ex.: Q4'); m.add_argument('--mes', required=True, help='ex.: Janeiro')
    m.add_argument('--ano', required=True); m.add_argument('--linha1', default='Balanço trimestral'); m.add_argument('--polos', default='Recife — São Paulo')
    m.add_argument('--sem-capa', action='store_true'); m.add_argument('--sem-agenda', action='store_true')
    sub.add_parser('componentes')
    a = ap.parse_args()
    if a.cmd == 'verificar':
        sys.exit(1 if verificar(a.arquivo).erros else 0)
    elif a.cmd == 'gerar':
        gerar(a.arquivo, a.saida)
    elif a.cmd == 'pendencias':
        pendencias(a.arquivo)
    elif a.cmd == 'pacote':
        pacote(a.parte, a.versao, a.saida, a.edicao)
    elif a.cmd == 'montar':
        montar(a.partes, a.saida, a.trimestre, a.mes, a.ano, a.linha1, a.polos, not a.sem_capa, not a.sem_agenda)
    elif a.cmd == 'componentes':
        componentes()


if __name__ == '__main__':
    main()
