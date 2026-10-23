#!/usr/bin/env python
"""Migra todo el libro publicado (el contenido de _toc.yml) de Jupyter Book a Quarto.

Uso (desde quarto/):  python tools/convert_book.py
Lee los .md originales (en la raiz del repo, un nivel arriba) y escribe los .qmd manteniendo las mismas rutas.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent                      # quarto/
REPO = OUT.parent                      # raiz del repo
CONVERTER = HERE / 'convert_chapter.py'

DATA_PKGS = 'numpy,scipy,matplotlib,seaborn,pandas,statsmodels'

# (fuente, destino, opciones del conversor)
CHAPTERS = [
    ('front.md',                                                   'index.qmd',                                                  ['--engine', 'markdown', '--unnumbered-title']),
    ('chapter1_intro/intro/intro.md',                              'chapter1_intro/intro/intro.qmd',                             ['--engine', 'markdown']),
    ('chapter1_intro/repaso_de_probabilidad/repaso_de_probabilidad.md',
                                                                   'chapter1_intro/repaso_de_probabilidad/repaso_de_probabilidad.qmd',
                                                                   ['--live', '1,2,3,4,5', '--packages', 'numpy,scipy,matplotlib,seaborn']),
    ('chapter2_aed/datos_y_variables.md',                         'chapter2_aed/datos_y_variables.qmd',                         ['--engine', 'markdown']),
    ('chapter2_aed/analisis_exploratorio.md',                     'chapter2_aed/analisis_exploratorio.qmd',                     ['--live', 'all', '--packages', DATA_PKGS]),
]

ok = True
for src, dst, opts in CHAPTERS:
    r = subprocess.run([sys.executable, str(CONVERTER), str(REPO / src), str(OUT / dst), *opts],
                       capture_output=True, text=True, encoding='utf-8')
    print(r.stdout.strip() or r.stderr.strip())
    ok &= r.returncode == 0
sys.exit(0 if ok else 1)
