#!/usr/bin/env python
"""Convierte un capitulo MyST (Jupyter Book) a Quarto (.qmd).

Uso:
  python tools/convert_chapter.py <entrada.md> <salida.qmd> [--engine jupyter|markdown]
         [--live none|all|1,2,3] [--packages numpy,scipy,...] [--unnumbered-title]

Preserva la prosa tal cual; traduce directivas y roles MyST a la sintaxis de Quarto, genera los
gemelos HTML/PDF de las celdas editables y copia solo las imagenes que el capitulo usa.
"""
import argparse
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).parent
FENCE_OPEN = re.compile(r'^(\s*)(`{3,}|:{3,})\s*\{([\w\-]+)\}\s*(.*)$')
FENCE_CLOSE = re.compile(r'^\s*(`{3,}|:{3,})\s*$')
OPTION = re.compile(r'^:([\w\-]+):\s*(.*)$')
WIDGET_CELL_MARK = 'bokeh_plots'           # la celda que usa Bokeh se reemplaza por el widget JS
CALLOUT_KINDS = ('tip', 'important', 'warning', 'note', 'caution')


@dataclass
class Dir:
    name: str
    arg: str
    opts: dict = field(default_factory=dict)
    body: list = field(default_factory=list)


def parse(lines):
    nodes, text, i = [], [], 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if not m:
            text.append(lines[i]); i += 1; continue
        if text:
            nodes.append('\n'.join(text)); text = []
        fence, name, arg = m.group(2), m.group(3), m.group(4).strip()
        j = i + 1
        while j < len(lines):
            c = FENCE_CLOSE.match(lines[j])
            if c and c.group(1)[0] == fence[0] and len(c.group(1)) >= len(fence):
                break
            j += 1
        body = lines[i + 1:j]
        opts = {}
        while body and OPTION.match(body[0]):
            k, v = OPTION.match(body[0]).groups(); opts[k] = v.strip(); body = body[1:]
        if body and not body[0].strip():
            body = body[1:]
        nodes.append(Dir(name, arg, opts, body))
        i = j + 1
    if text:
        nodes.append('\n'.join(text))
    return nodes


# ---------------------------------------------------------------- texto
INLINE_MATH = re.compile(r'(?<!\$)\$(?!\$)([^$\n]+?)(?<!\$)\$(?!\$)')
PAREN_MATH = re.compile(r'\\\(\s*(.+?)\s*\\\)')
HTML_LINK = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>')
ROLE_REF = re.compile(r'\{ref\}`ex-([\w\-]+)`')
ROLE_CITE = re.compile(r'\{cite\}`([^`]+)`')
IMG_LINE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$')
LIST_ITEM = re.compile(r'^\s*([-*+]|\d+[.)])\s+\S')


def div(attrs, body):
    longest = max([len(m) for m in re.findall(r'(?m)^(:{3,})', body)] or [2])
    f = ':' * max(3, longest + 1)
    return f'{f} {{{attrs}}}\n\n{body.strip()}\n\n{f}\n\n'


def cite(m):
    keys = [k.strip() for k in m.group(1).split(',')]
    return '[' + '; '.join('@' + k for k in keys) + ']'


def fix_text(block):
    out, in_display, prev = [], False, ''
    for line in block.split('\n'):
        s = line.strip()
        if s == '$$':
            in_display = not in_display; out.append(line); prev = line; continue
        if in_display or '$$' in line:
            out.append(line); prev = line; continue
        if s == '---':                                   # evita que pandoc lo lea como bloque YAML
            out.append('* * *'); prev = line; continue
        if LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev) and not prev.startswith((' ', '\t', '|', '>')):
            out.append('')                               # pandoc exige linea en blanco antes de una lista
        line = PAREN_MATH.sub(lambda m: '$' + m.group(1) + '$', line)
        line = INLINE_MATH.sub(lambda m: '$' + m.group(1).strip() + '$', line)
        line = HTML_LINK.sub(lambda m: f'[{m.group(2)}]({m.group(1)})', line)
        line = ROLE_REF.sub(lambda m: '@exr-' + m.group(1), line)
        line = ROLE_CITE.sub(cite, line)
        if 'img.shields.io' in line:                     # insignias remotas (SVG): solo en HTML
            out.append(div('.content-visible when-format="html"', line).rstrip('\n')); out.append(''); prev = ''
            continue
        im = IMG_LINE.match(line)
        if im:
            path = im.group(2).replace('//', '/')
            alt = im.group(1).replace('"', "'")
            if path.lower().endswith('.gif'):            # LaTeX no admite GIF: HTML animado, PDF con un cuadro estatico
                still = path[:-4] + '_frame.png'
                out.append(div('.content-visible when-format="html"', f'![]({path}){{fig-alt="{alt}"}}').rstrip('\n'))
                out.append('')
                out.append(div('.content-visible unless-format="html"', f'![]({still}){{fig-alt="{alt}"}}').rstrip('\n'))
                out.append(''); prev = ''
                continue
            line = f'![]({path}){{fig-alt="{alt}"}}'
        out.append(line)
        prev = line
    return '\n'.join(out)


# ---------------------------------------------------------------- emision
class Converter:
    def __init__(self, src_dir, live):
        self.src_dir = Path(src_dir)
        self.live = live                       # 'none' | 'all' | set de indices
        self.cell_n = 0
        self.stats = {'cells': 0, 'live_twins': 0, 'widget': 0, 'calc_fig': 0, 'admonitions': 0,
                      'exercises': 0, 'figures': 0, 'cards': 0, 'cites': 0}

    def is_live(self, n):
        return self.live == 'all' or (isinstance(self.live, set) and n in self.live)

    def nodes(self, nodes):
        return ''.join(self.node(n) for n in nodes)

    def node(self, n):
        if isinstance(n, str):
            return fix_text(n) + '\n'
        return getattr(self, 'd_' + n.name.replace('-', '_'), self.d_unknown)(n)

    def d_unknown(self, d):
        raise SystemExit(f'Directiva no soportada: {d.name}')

    def body(self, d):
        return self.nodes(parse(d.body))

    # --- bloques de texto
    def callout(self, kind, title, body, dropdown=False):
        self.stats['admonitions'] += 1
        title = re.sub(r'"([^"]*)"', '\u201c\\1\u201d', title)     # comillas dentro de un atributo rompen el div
        attrs = f'.callout-{kind}' + (f' title="{title}"' if title else '') + (' collapse="true"' if dropdown else '')
        return div(attrs, body)

    def d_admonition(self, d):
        cls = [c.strip() for c in d.opts.get('class', 'note').split(',')]
        kind = next((c for c in cls if c in CALLOUT_KINDS), 'note')
        return self.callout(kind, d.arg, self.body(d), 'dropdown' in cls)

    def _simple_admonition(self, d):                 # ```{note} / ```{tip} ...
        return self.callout(d.name, d.arg, self.body(d), 'dropdown' in d.opts.get('class', ''))
    d_note = d_tip = d_important = d_warning = d_caution = _simple_admonition

    def d_epigraph(self, d):
        lines = [l for l in d.body if l.strip()]
        author = lines[-1].lstrip('- ').strip() if lines and lines[-1].lstrip().startswith('--') else ''
        quote = ' '.join(l.strip() for l in lines if not l.lstrip().startswith('--'))
        return f'> {quote}\n>\n> — {author}\n\n'

    def card_div(self, title, body):
        self.stats['cards'] += 1
        head = div('.card-header', title) if title else ''
        return div('.card', head + div('.card-body', body))

    def d_card(self, d):
        return self.card_div(d.arg, self.body(d))

    def d_grid(self, d):
        items = [n for n in parse(d.body) if isinstance(n, Dir) and n.name in ('grid-item', 'grid-item-card')]
        default = max(1, 12 // max(1, len(items)))
        out = ''
        for it in items:
            cols = it.opts.get('columns', str(default))
            inner = self.card_div(it.arg, self.body(it)) if it.name == 'grid-item-card' else self.body(it)
            out += div(f'.g-col-12 .g-col-md-{cols}', inner)
        return div('.grid', out)

    def d_rubric(self, d):
        return f'## {d.arg} {{.unnumbered}}\n\n'

    def d_bibliography(self, d):
        return '::: {#refs}\n:::\n\n'

    def scaled_width(self, path, scale):
        try:
            from PIL import Image
            f = float(re.sub(r'[^\d.]', '', scale)) / 100
            with Image.open(self.src_dir / path) as im:
                return round(im.width * f)
        except Exception:
            return None

    def d_figure(self, d):
        self.stats['figures'] += 1
        name = d.opts.get('name', '')
        if name == 'fig-calculo-probabilidades':
            self.stats['calc_fig'] += 1
            return (HERE / 'snippets' / 'fig_calculo.qmd').read_text(encoding='utf-8') + '\n'
        path = d.arg.replace('//', '/')
        caption = ' '.join(l.strip() for l in d.body if l.strip())
        attrs = []
        if name:
            attrs.append('#' + (name if name.startswith('fig-') else 'fig-' + name))
        if 'height' in d.opts:
            attrs.append(f'height={d.opts["height"]}')
        if 'scale' in d.opts:
            w = self.scaled_width(path, d.opts['scale'])
            if w:
                attrs.append(f'width={w}px')
        if 'alt' in d.opts:
            attrs.append('fig-alt="' + d.opts['alt'].replace('"', "'") + '"')
        return f'![{caption}]({path})' + (f'{{{" ".join(attrs)}}}' if attrs else '') + '\n\n'

    def d_exercise(self, d):
        self.stats['exercises'] += 1
        label = d.opts.get('label', 'x')
        ident = 'exr-' + (label[3:] if label.startswith('ex-') else label)
        children = parse(d.body)
        sols = [c for c in children if isinstance(c, Dir) and c.name == 'solution']
        rest = [c for c in children if not (isinstance(c, Dir) and c.name == 'solution')]
        out = div(f'#{ident}', self.nodes(rest))
        for s in sols:
            out += div('.callout-note title="Solución" collapse="true"', self.nodes(parse(s.body)))
        return out

    def d_solution(self, d):          # solo se llega aqui si la solucion no esta anidada
        return div('.callout-note title="Solución" collapse="true"', self.body(d))

    def d_code_block(self, d):
        return f'```{d.arg}\n' + '\n'.join(d.body).rstrip() + '\n```\n\n'

    # --- celdas de codigo
    def d_code_cell(self, d):
        self.cell_n += 1
        self.stats['cells'] += 1
        code = '\n'.join(d.body).strip('\n')
        if WIDGET_CELL_MARK in code:
            self.stats['widget'] += 1
            return (HERE / 'snippets' / 'widget_distribuciones.qmd').read_text(encoding='utf-8') + '\n'
        hide = 'remove-input' in d.opts.get('tags', '')
        if self.is_live(self.cell_n) and not hide:
            self.stats['live_twins'] += 1
            live = f'```{{pyodide}}\n#| autorun: true\n{code}\n```'
            static = f'```{{python}}\n{code}\n```'
            return (div('.content-visible when-format="html"', live) +
                    div('.content-visible unless-format="html"', static))
        head = '#| echo: false\n' if hide else ''
        return f'```{{python}}\n{head}{code}\n```\n\n'


def convert(src, src_dir, live='none', engine='jupyter', packages=(), unnumbered_title=False):
    lines = src.splitlines()
    if lines and lines[0].strip() == '---':          # quitar front matter jupytext
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
        lines = lines[end + 1:]
    while lines and lines[-1].strip() in ('', '---'):
        lines.pop()
    conv = Converter(src_dir, live)
    body = conv.nodes(parse(lines))
    body = re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'
    if unnumbered_title:
        body = re.sub(r'^(# .+?)\s*$', r'\1 {.unnumbered}', body, count=1, flags=re.M)
    head = []
    if engine == 'jupyter':
        head += ['engine: jupyter', 'jupyter: python3']
    if packages:
        head += ['pyodide:', '  packages:'] + [f'    - {p}' for p in packages]
    front = ('---\n' + '\n'.join(head) + '\n---\n\n') if head else ''   # un bloque YAML vacio rompe el titulo del capitulo
    return front + body, conv.stats


def copy_assets(qmd_text, src_dir, out_dir):
    """Copia solo las imagenes que el capitulo referencia (y genera el cuadro fijo de los GIF)."""
    copied, missing = [], []
    for rel in sorted(set(re.findall(r'\]\(((?:\.\./)*figuras/[^)\s]+)\)', qmd_text))):
        src, dst = src_dir / rel, out_dir / rel
        if rel.endswith('_frame.png') and not src.exists():
            gif = src_dir / (rel[:-len('_frame.png')] + '.gif')
            if gif.exists():
                from PIL import Image
                im = Image.open(gif); im.seek(getattr(im, 'n_frames', 1) // 2)
                dst.parent.mkdir(parents=True, exist_ok=True); im.convert('RGB').save(dst); copied.append(rel)
                continue
        if src.exists():
            if not dst.exists() or dst.stat().st_size != src.stat().st_size:
                dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(src, dst); copied.append(rel)
        elif not dst.exists():
            missing.append(rel)
    return copied, missing


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('src'); ap.add_argument('dst')
    ap.add_argument('--engine', default='jupyter', choices=['jupyter', 'markdown'])
    ap.add_argument('--live', default='none')
    ap.add_argument('--packages', default='')
    ap.add_argument('--unnumbered-title', action='store_true')
    a = ap.parse_args()
    live = a.live if a.live in ('none', 'all') else {int(x) for x in a.live.split(',')}
    src, dst = Path(a.src), Path(a.dst)
    text, st = convert(src.read_text(encoding='utf-8'), src.parent, live, a.engine,
                       [p for p in a.packages.split(',') if p], a.unnumbered_title)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding='utf-8', newline='\n')
    copied, missing = copy_assets(text, src.parent, dst.parent)
    print(dst.name, st, '| assets copiados:', len(copied), '| faltantes:', missing)
