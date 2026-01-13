# LaTeX Thesis Guide - Understanding Your Script

## Table of Contents
1. [Document Structure Overview](#document-structure-overview)
2. [Preamble Section](#preamble-section)
3. [Title Page](#title-page)
4. [Front Matter](#front-matter)
5. [Main Content](#main-content)
6. [Common Commands](#common-commands)
7. [Troubleshooting](#troubleshooting)

---

## Document Structure Overview

Your LaTeX document has four main parts:

```
1. PREAMBLE (lines 1-76)     → Document settings and packages
2. TITLE PAGE (lines 79-113)  → Formal thesis title page
3. FRONT MATTER (lines 115-154) → Abstract and Table of Contents
4. MAIN CONTENT (line 161+)    → Your actual thesis chapters
```

---

## Preamble Section

### 1. Document Class
```latex
\documentclass[]{article}
```
**What it does:** Tells LaTeX this is an article-style document (other options: book, report)

### 2. Essential Packages

#### Math Support
```latex
\usepackage{amsmath,amssymb}
```
- `amsmath`: Advanced math equations
- `amssymb`: Math symbols like ≥, ∑, ∫

#### Unicode Characters
```latex
\usepackage{newunicodechar}
\newunicodechar{⁻}{\textsuperscript{-}}
\newunicodechar{α}{\ensuremath{\alpha}}
```
**What it does:** Converts Unicode symbols to LaTeX commands
- ⁻ becomes superscript minus
- α becomes Greek alpha

#### Font Encoding
```latex
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
```
**What it does:** 
- `fontenc`: Better font rendering
- `inputenc`: Allows UTF-8 characters (accents, special characters)

#### Graphics
```latex
\usepackage{graphicx}
```
**What it does:** Allows you to insert images with `\includegraphics{}`

#### Hyperlinks
```latex
\usepackage{hyperref}
\hypersetup{
  hidelinks,
  pdfcreator={LaTeX via pandoc}
}
```
**What it does:** Makes clickable links in PDF (table of contents, references)
- `hidelinks`: Removes colored boxes around links

### 3. Document Settings

#### Section Numbering
```latex
\setcounter{secnumdepth}{3}
```
**What it does:** Enables numbering for sections (1., 1.1, 1.1.1)
- 0 = chapters only
- 1 = sections (1., 2., 3.)
- 2 = subsections (1.1, 1.2)
- 3 = subsubsections (1.1.1, 1.1.2)

---

## Title Page

### Structure
```latex
\begin{titlepage}
\begin{center}
  % Content here
\end{center}
\end{titlepage}
```

### Key Commands

#### Vertical Spacing
```latex
\vspace*{2cm}    % Fixed space from top
\vspace{3cm}     % Flexible vertical space
```

#### Text Formatting
```latex
{\Large\bfseries YOUR TITLE}
```
- `\Large`: Large font size
- `\bfseries`: Bold font
- `{}`: Groups formatting to apply only to enclosed text

#### Line Breaks
```latex
Louisiana State University and\\
Agricultural and Mechanical College\\
```
- `\\`: Forces a new line
- `\\\\`: Creates blank line (not recommended, use `\vspace` instead)

### What to Customize
Replace these placeholders:
```latex
by\\
[Your Name]\\                              % → Your full name
[Your Previous Degree and Institution]\\   % → B.S. Civil Eng, LSU, 2020
[Month Year]                               % → May 2025
```

---

## Front Matter

### Page Numbering
```latex
\pagenumbering{roman}    % i, ii, iii, iv...
\setcounter{page}{2}     % Start at page ii
```

Then later:
```latex
\pagenumbering{arabic}   % 1, 2, 3, 4...
\setcounter{page}{1}     % Restart at page 1
```

**Why?** Thesis format requires:
- Title page: unnumbered
- Abstract, TOC: roman numerals (ii, iii, iv...)
- Main content: arabic numbers (1, 2, 3...)

### Abstract
```latex
\section*{Abstract}              % Section without number
\addcontentsline{toc}{section}{Abstract}  % Add to Table of Contents
```
- `*` prevents numbering
- `\addcontentsline` manually adds it to TOC

### Table of Contents
```latex
\tableofcontents
```
**What it does:** Automatically generates TOC from all `\section`, `\subsection`, etc.

### Page Breaks
```latex
\newpage
```
**What it does:** Starts a new page

---

## Main Content

### Sections
```latex
\section{Introduction}           % Numbered section (1.)
\subsection{Background}          % Numbered subsection (1.1)
\subsubsection{Details}          % Numbered subsubsection (1.1.1)
```

### Text Formatting

#### Emphasis
```latex
\textbf{bold text}      % Bold
\textit{italic text}    % Italic
\emph{emphasized}       % Emphasis (usually italic)
```

#### Special Characters
```latex
\%    % Percent sign
\_    % Underscore
\&    % Ampersand
\$    % Dollar sign
```

### Lists

#### Numbered List
```latex
\begin{enumerate}
\item First item
\item Second item
\end{enumerate}
```

#### Bullet List
```latex
\begin{itemize}
\item Bullet point
\item Another point
\end{itemize}
```

### Images
```latex
\includegraphics[width=6.5in,height=4.5in]{media/image1.png}
```

**Options:**
- `width=`: Set width
- `height=`: Set height
- `scale=0.5`: Scale to 50%
- `keepaspectratio`: Maintain aspect ratio

**Better image insertion:**
```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{media/image1.png}
  \caption{Your caption here}
  \label{fig:myimage}
\end{figure}
```
- `[htbp]`: Placement (here, top, bottom, page)
- `\centering`: Center the image
- `\caption`: Add caption
- `\label`: Reference with `\ref{fig:myimage}`

### Math Equations

#### Inline Math
```latex
The equation $E = mc^2$ is famous.
```

#### Display Math
```latex
\begin{equation}
E = mc^2
\end{equation}
```

---

## Common Commands

### References
```latex
% Citation
(Author et al., 2023)

% In LaTeX with bibliography:
\cite{author2023}
```

### Special Spacing
```latex
\noindent      % No paragraph indent
\par           % New paragraph
\bigskip       % Big vertical space
\medskip       % Medium vertical space
\smallskip     % Small vertical space
```

### Quotes
```latex
``double quotes''     % Proper left and right quotes
`single quote'        % Proper single quotes
```

---

## Troubleshooting

### Common Errors

#### 1. "Undefined control sequence"
**Problem:** Typo in command name
```latex
\secton{Title}    % Wrong
\section{Title}   % Correct
```

#### 2. "Missing $ inserted"
**Problem:** Special character not escaped
```latex
Use _ in text       % Wrong
Use \_ in text      % Correct
```

#### 3. "File not found"
**Problem:** Image path wrong
```latex
% Make sure file exists:
\includegraphics{media/image1.png}

% Check spelling and extension (.png, .jpg, .jpeg)
```

#### 4. Unicode character errors
**Already fixed in your document!** The `\newunicodechar` commands handle this.

### Compilation Tips

#### Compile Order
For complete document with TOC:
```bash
pdflatex main_thesis.tex   # First pass
pdflatex main_thesis.tex   # Second pass (updates TOC)
```

#### Quick Compile
```bash
pdflatex main_thesis.tex
```

#### With Bibliography
```bash
pdflatex main_thesis.tex
bibtex main_thesis
pdflatex main_thesis.tex
pdflatex main_thesis.tex
```

### Check PDF
```bash
evince main_thesis.pdf      # Linux
open main_thesis.pdf        # Mac
start main_thesis.pdf       # Windows
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| New section | `\section{Title}` |
| New subsection | `\subsection{Title}` |
| Bold text | `\textbf{text}` |
| Italic text | `\textit{text}` |
| New page | `\newpage` |
| Insert image | `\includegraphics{path}` |
| Bullet list | `\begin{itemize}...\end{itemize}` |
| Numbered list | `\begin{enumerate}...\end{enumerate}` |
| Math inline | `$equation$` |
| Math display | `\begin{equation}...\end{equation}` |
| Comment | `% This is a comment` |
| Force space | `\␣` (backslash space) |
| Non-breaking space | `~` (tilde) |

---

## Advanced Tips

### 1. Conditional Compilation
Only compile specific sections during editing:
```latex
\includeonly{chapter1,chapter2}  % In preamble
\include{chapter1}               % In document
\include{chapter2}
```

### 2. Custom Commands
Create shortcuts:
```latex
\newcommand{\insar}{PS-InSAR}    % In preamble

% Then use:
\insar{} instead of typing "PS-InSAR" each time
```

### 3. Better Tables
```latex
\begin{table}[htbp]
\centering
\begin{tabular}{|l|c|r|}
\hline
Left & Center & Right \\
\hline
Data & More & Info \\
\hline
\end{tabular}
\caption{My table}
\label{tab:mytable}
\end{table}
```

---

## File Organization

### Recommended Structure
```
Thesis_work/
├── main_thesis.tex           # Main file
├── chapters/
│   ├── introduction.tex
│   ├── literature_review.tex
│   └── methodology.tex
├── media/
│   ├── image1.png
│   └── image2.png
└── references.bib           # Bibliography
```

### Split Large Files
In `main_thesis.tex`:
```latex
\input{chapters/introduction.tex}
\input{chapters/literature_review.tex}
```

---

## Getting Help

### Resources
1. **Overleaf Documentation**: https://www.overleaf.com/learn
2. **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX
3. **TeX Stack Exchange**: https://tex.stackexchange.com/

### Package Documentation
View any package docs:
```bash
texdoc packagename
# Example:
texdoc amsmath
texdoc graphicx
```

---

## Summary Checklist

Before submitting your thesis:

- [ ] Fill in your name, degree, and date on title page (lines 108-110)
- [ ] Compile twice to update Table of Contents
- [ ] Check all images display correctly
- [ ] Verify page numbering (roman for front matter, arabic for content)
- [ ] Spell check (use `aspell check main_thesis.tex`)
- [ ] Check PDF renders correctly
- [ ] Verify all Unicode characters display properly
- [ ] Add bibliography if needed
- [ ] Check university thesis formatting requirements

---

**Need More Help?**
- Read the comments in your `.tex` file (lines starting with `%`)
- Try small changes and recompile to see the effect
- Keep backups before major edits!

**Good luck with your thesis! 🎓**
