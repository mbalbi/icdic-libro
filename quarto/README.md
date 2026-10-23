# Quarto edition of the book

This folder is the Quarto version of *Introducción a la Ciencia de Datos para Ingeniería Civil*.
The Jupyter Book sources in the repository root are untouched; the `.qmd` files here are
**generated** from the original `.md` files (see "Editing" below).

## Requirements

- [Quarto](https://quarto.org) 1.10 or newer (built and tested with 1.10.19)
- Python 3.12 with the packages in `requirements.txt`
  (`python -m venv .venv && .venv/Scripts/pip install -r requirements.txt`)
- A LaTeX distribution for the PDF (`quarto install tinytex`)
- Node.js, only to run the JS-vs-scipy parity test

## Build

```powershell
$env:QUARTO_PYTHON = ".venv/Scripts/python.exe"   # Python used to run the code cells
quarto render --to live-html                      # interactive site  -> _site/
quarto render --to pdf --output-dir _pdf          # PDF edition       -> _pdf/
quarto preview --to live-html                     # live preview
```

The HTML must be served over `http://` (use `quarto preview`, or `python -m http.server --directory _site`);
opening the files directly from disk does not work because Pyodide and the OJS runtime need a web server.

## What is interactive

| Piece | Where it runs | Notes |
|---|---|---|
| Sliders and the distribution plotter | Browser, JavaScript | Instant (about 20-30 ms per update). Math lives in `chapter1_intro/repaso_de_probabilidad/figuras/distribuciones.js` |
| Editable Python cells | Browser, Pyodide (WebAssembly) | `autorun`; about 1 minute to start on a cold cache |
| Everything else | Build time | Executed by Quarto, shown as static output |

Every live cell has a **PDF twin**: the same code executed at build time (`content-visible` blocks),
because Pyodide cells do not exist in the PDF.

## JS math is tested against scipy

```powershell
python chapter1_intro/repaso_de_probabilidad/figuras/generar_referencia.py ref.json
node  chapter1_intro/repaso_de_probabilidad/figuras/test_paridad.mjs ref.json
```

All five distributions (Normal, LogNormal, Exponential, Beta, Gumbel) must print `ALL PASS`
(max error about 1e-14). Run this whenever `distribuciones.js` changes.

## Editing: the `.qmd` files are generated

Edit the original MyST sources in the repository root, then regenerate:

```powershell
python tools/convert_book.py
```

`tools/convert_chapter.py` translates MyST (admonitions, cards/grids, figures, exercises, citations,
code cells) to Quarto and copies only the images each chapter uses. Per-chapter options (which cells
are live, which Pyodide packages to load) are in `tools/convert_book.py`.
Hand-written pieces that replace non-portable content live in `tools/snippets/`.
If you prefer to maintain the `.qmd` files by hand from now on, delete the generated header
and stop running the converter.

## Known limits

- Pyodide 0.28 (used by Quarto Live) has no geopandas/pyproj, PyMC/PyTensor/ArviZ, or ipywidgets.
  Pyodide's pandas/statsmodels versions are older than the ones used at build time.
- Save `.qmd` files as UTF-8 **without BOM** (a BOM silently breaks the header and OJS blocks).
- Quarto attributes cannot contain nested double quotes (the converter handles this for callout titles).
