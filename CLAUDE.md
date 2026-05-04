# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This is a master's thesis from Northeastern University (东北大学), written in LaTeX. The thesis topic is **degradation modeling and fault diagnosis for EV key components based on unbiased uncertainty quantification**. The LaTeX template is derived from [NEU-Thesis](https://github.com/sci-m-wang/NEU-Thesis), which is based on `neuthesis`.

## Build

```bash
# Quick build (xelatex only, no bibliography refresh)
./build.sh x Thesis

# Full build chain (xelatex → bibtex → xelatex → xelatex)
./build.sh xa Thesis
```

The `build.sh` script uses `xelatex` as the compiler. Add `a` to the first argument to run bibtex as part of the build chain. Output goes to `Tmp/` directory.

## Repository structure

- `Thesis.tex` — main entry point: document class, packages, and `\include` order
- `Tex/` — all chapter `.tex` files
  - `Mainmatter.tex` — controls which chapters are included
  - `Frontpages.tex` — title page metadata (author, advisor, degree, dates, etc.)
  - `Introduction.tex`, `HSSTT.tex`, `RODTNet.tex`, `DA-TMLLM.tex` — Chapters 1–4 (the three core papers + introduction)
  - `Conclusions.tex` — Chapter 5 (summary & outlook)
  - `Backmatter.tex` — acknowledgements, publications, patents, awards
  - `Abstract.tex` — Chinese and English abstracts
  - `Chap_Intro.tex`, `Chap_Guide.tex`, `Chap_Format.tex` — template guide chapters (commented out in Mainmatter.tex)
- `Style/` — document class and style files
  - `neuthesis.cls` — the core document class (NEU thesis formatting)
  - `neuthesis.cfg` — configuration overrides
  - `artratex.sty` — package wrapper (bibtex, geometry, headers, tables, math, etc.)
  - `artracom.sty` — user-defined commands
- `Biblio/ref.bib` — all references in BibTeX format
  - `check_bib_format.py` — validates entries against GB/T 7714-2015 standard
  - `fix_bib_format.py` — auto-fixes author count, year/page formatting, journal abbreviations
  - `abbreviation_mapping.csv` — journal abbreviation → full name mapping
- `Img/` — figures organized by chapter: `Intro_figures/`, `HSSTT_figures/`, `RODTNet_figures/`, `DA-TMLLM_figures/`
- `Fonts/` — Chinese fonts (simfang, simhei, simkai, simsun) required by the template's `fontset=windows` option

## Key macros

- `\review{text}` — renders text in red (for annotation/editing)
- `\reviewORprint{review version}{print version}` — toggles content between blind-review and final print versions; controlled by the `printcopy` class option
  - When `printcopy` is **absent** (blind review): the first argument is used
  - When `printcopy` is **present**: the second argument is used

## Bibliography workflow

1. Edit `Biblio/ref.bib` directly for adding/updating references
2. Run `python3 Biblio/check_bib_format.py` to find GB/T 7714-2015 compliance issues
3. Run `python3 Biblio/fix_bib_format.py` to auto-fix format issues
4. Full rebuild with bibliography: `./build.sh xa Thesis`

The bibliography style file is `Biblio/gbt7714-unsrt.bst` (GB/T 7714-2015, unsorted/numeric).

## Translation and editing guidelines

`prompts.md` contains detailed Chinese-language instructions for academic translation and editing tasks. Key rules when editing the Chinese text in `.tex` files:

- No first-person pronouns (我/我们); use third-person or passive voice
- Chinese-English spacing: add a half-width space between Chinese characters and English letters/abbreviations/numbers (e.g., "高可信 SOH 估计")
- After an abbreviation is defined, use only the abbreviation; do not append English full spelling in parentheses
- Do not add intensifiers (显著/深入/极大) that don't exist in the original text
- Journal abbreviations should expand to full names in the bibliography per GB/T 7714-2015

## Important notes

- The compiler **must** be `xelatex` (not pdflatex) due to Chinese font handling
- `Tmp/` is the build output directory; all intermediate files go there
- The `.gitignore` excludes build artifacts but **not** the fonts (`.ttf`/`.ttc`), though local font files are listed in `.gitignore` (simfang.ttf, etc.) — these are needed for compilation when system fonts are unavailable
- The template supports both `bibtex` and `biber` bibliography processors; this project uses `bibtex` (the `a` flag in `build.sh`)
