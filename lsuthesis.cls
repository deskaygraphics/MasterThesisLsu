%%
%% This is file `lsuthesis.cls', a LaTeX class derived from `book.cls'.
%%
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{lsuthesis}[2025/12/20 LSU Thesis Class]
% We want ``book'' class but with ``12pt'' and ``oneside'' as default
% options, unless the user specifies different values. Thus we have
% to process such options ourselves, with our own defaults, and then
% pass them along to the subclass. We also define options specific to
% our class.
\newcommand\@lsuthesisptsize{12pt}
\newif\if@lsuthesissizes\@lsuthesissizestrue
\DeclareOption{10pt}{\renewcommand\@lsuthesisptsize{10pt}\@lsuthesissizesfalse}
\DeclareOption{11pt}{\renewcommand\@lsuthesisptsize{11pt}\@lsuthesissizesfalse}
\DeclareOption{12pt}{\renewcommand\@lsuthesisptsize{12pt}\@lsuthesissizesfalse}
\newcommand\@lsuthesissided{oneside}
\DeclareOption{oneside}{\renewcommand\@lsuthesissided{oneside}}
\DeclareOption{twoside}{\renewcommand\@lsuthesissided{twoside}}
\newif\if@lsuthesisdoublespace\@lsuthesisdoublespacefalse
\DeclareOption{singlespacing}{\@lsuthesisdoublespacefalse}
\DeclareOption{doublespacing}{\@lsuthesisdoublespacetrue}
\newif\if@lsuthesisraggedright\@lsuthesisraggedrighttrue
\DeclareOption{flushright}{\@lsuthesisraggedrightfalse}
\DeclareOption{raggedright}{\@lsuthesisraggedrighttrue}
%% Remove next line? What options get passed through? Perhaps explicitly
%% define those as above, the ones that are documented in our own
%% documentation, and have no support for any others!
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\PassOptionsToClass{\@lsuthesisptsize,\@lsuthesissided}{book}
\LoadClass{book}[2014/09/29]


%% The LuaLaTeX engine uses UTF8 input encoding and Latin Modern
%% fonts that work at any size (as compared to Computer Modern, which
%% substitute particular sizes). The CMU fonts improve on Latin Modern
%% with more Unicode code points.
\usepackage{ifluatex}
\ifluatex
  \usepackage{fontspec}
  \setmainfont{CMU Serif}
  \setsansfont{CMU Sans Serif}
  \setmonofont{CMU Typewriter Text}
\else
  \usepackage[utf8]{inputenc}
  \usepackage[T1]{fontenc}
  \usepackage{lmodern}
\fi


%% To make the List of Tables, List of Figures, and Bibliography all
%% appear in the Table of Contents.
\usepackage[nottoc]{tocbibind}


% LSU requires 1in margins throughout.
% Old way:
%\oddsidemargin=0in \textwidth=6.5 in \topmargin=-0.4in
%\textheight=9in \footskip=0.72in \headheight=12pt \headsep=10pt
% New way below. To see the results when trying changes, temporarily
% run a test document with \usepackage{layout} and then do \layout
% inside the document. (Also turn on ``twoside'' option to see a
% two-sided layout.)

\setlength\@tempdima{\paperwidth}
\addtolength\@tempdima{-2in} % 1in left and 1in right margin
\setlength\textwidth{\@tempdima}
\@settopoint\textwidth

\setlength\@tempdima{\paperheight}
\addtolength\@tempdima{-2in} % 1in top and 1in bottom margin
\divide\@tempdima\baselineskip
\@tempcnta=\@tempdima
\setlength\textheight{\@tempcnta\baselineskip}

\addtolength\textheight{\topskip}
\if@twoside
  \setlength\@tempdima        {\paperwidth}
  \addtolength\@tempdima      {-\textwidth}
  \setlength\oddsidemargin    {.4\@tempdima}
  \addtolength\oddsidemargin  {-1in}
  \setlength\marginparwidth   {.6\@tempdima}
\else
  \setlength\@tempdima        {\paperwidth}
  \addtolength\@tempdima      {-\textwidth}
  \setlength\oddsidemargin    {.5\@tempdima}
  \addtolength\oddsidemargin  {-1in}
  \setlength\marginparwidth   {.5\@tempdima}
\fi
\addtolength\marginparwidth {-\marginparsep}
\addtolength\marginparwidth {-0.1in} % printer margin
\ifdim \marginparwidth >2in
   \setlength\marginparwidth{2in}
\fi
\@settopoint\oddsidemargin
\@settopoint\marginparwidth
\setlength\evensidemargin  {\paperwidth}
\addtolength\evensidemargin{-2in}
\addtolength\evensidemargin{-\textwidth}
\addtolength\evensidemargin{-\oddsidemargin}
\@settopoint\evensidemargin

\setlength\topmargin{\paperheight}
\addtolength\topmargin{-2in}
\addtolength\topmargin{-\headheight}
\addtolength\topmargin{-\headsep}
\addtolength\topmargin{-\textheight}
\addtolength\topmargin{-\footskip}
\addtolength\topmargin{-.5\topmargin}
\@settopoint\topmargin


%% Indentation-related matters.
%%
%% With 1in margins, we should have 0.5in paragraph indentations. However,
%% much of ``book'' has hardcoded 1.5em indents in various places. We move
%% this to a variable in case we want to make consistent indent changes.
%\parindent=.5in
\newdimen\@lsuparindent
\newdimen\@lsulistindent
\@lsuparindent=.5in
\@lsulistindent=\@lsuparindent
\parindent\@lsuparindent

\leftmargini\@lsulistindent
\leftmarginii\@lsulistindent
\leftmarginiii\@lsulistindent
\leftmarginiv\@lsulistindent
\leftmarginv\@lsulistindent
\leftmarginvi\@lsulistindent
\def\@listi{\leftmargin\leftmargini
            \labelwidth\leftmargin
            \advance\labelwidth-\labelsep
            \parsep\baselineskip
            \topsep\baselineskip
            \itemsep\z@}
\let\@listI\@listi
\@listi
\def\@listii {\leftmargin\leftmarginii
              \labelwidth\leftmargin
              \advance\labelwidth-\labelsep
              \topsep\z@
              \parsep\baselineskip
              \itemsep\z@}
\def\@listiii{\leftmargin\leftmarginiii
              \labelwidth\leftmargin
              \advance\labelwidth-\labelsep
              \topsep\z@
              \parsep\baselineskip
              %\partopsep \p@ \@plus\z@ \@minus\p@
              \itemsep\z@}
\def\@listiv{\leftmargin\leftmarginiv
              \labelwidth\leftmargin
              \advance\labelwidth-\labelsep
              \topsep\z@
              \parsep\baselineskip
              \itemsep\z@}



\renewenvironment{verse}
               {\let\\\@centercr
                \list{}{\itemsep      \z@
                        \itemindent   -\@lsuparindent
                        \listparindent\itemindent
                        \rightmargin  \leftmargin
                        \advance\leftmargin\@lsuparindent}%
                \item\relax}
               {\endlist}
\renewenvironment{quotation}
               {\list{}{\listparindent \@lsuparindent
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                \item\relax}
               {\endlist}

\if@lsuthesisdoublespace
\fi



%% Enter double-spacing mode if desired, and patch commands to match
%% LSU style. Package ``setspace'' already keeps certain elements (like
%% footnotes) single-spaced, but some things we must patch up ourselves.
\if@lsuthesisdoublespace
\usepackage{setspace}
%% For next line, see https://tex.stackexchange.com/questions/49880/equations-and-double-spacing
\setdisplayskipstretch{}
\renewcommand\doublespacing{\setstretch{2}}
\doublespacing
\usepackage{etoolbox}
\AtBeginEnvironment{thebibitemlist}{\singlespacing}
\AtBeginEnvironment{itemize}{\singlespacing}
\AtBeginEnvironment{enumerate}{\singlespacing}
\AtBeginEnvironment{description}{\singlespacing}
\AtBeginEnvironment{quote}{\singlespacing}
\AtBeginEnvironment{quotation}{\singlespacing}
\AtBeginEnvironment{verse}{\singlespacing}
%\AtBeginEnvironment{equation}{\setstretch{5}}
%\AtBeginEnvironment{array}{\setstretch{5}}
%\BeforeBeginEnvironment{equation}{\begingroup\setstretch{5}}
%\AfterEndEnvironment{equation}{\endgroup\noindent\ignorespaces}
%\AtBeginEnvironment{align}{\singlespacing}
%\def\singlespaceddisplay#1$${\begingroup\def\baselinestretch{5}#1\endgroup$$}
%\everydisplay{\def\baselinestretch{5}\par\relax}
%\let\oldlb\[
%\let\oldrb\]

\let\@lsu@starttoc\@starttoc
\def\@starttoc#1{\begingroup\singlespacing\unskip\@lsu@starttoc{#1}\endgroup}

\partopsep\z@
\def\@listi{\leftmargin\leftmargini
            \labelwidth\leftmargin
            \advance\labelwidth-\labelsep
            \topsep\z@
            \parsep\baselineskip
            \itemsep\z@}
\let\@listI\@listi
\@listi
\def\@listii{\leftmargin\leftmarginii
             \labelwidth\leftmargin
             \advance\labelwidth-\labelsep
             \topsep\z@
             \parsep\baselineskip
             \itemsep\z@}
\def\@listiii{\leftmargin\leftmarginiii
              \labelwidth\leftmargin
              \advance\labelwidth-\labelsep
              \topsep\z@
              \parsep\baselineskip
              \itemsep\z@}
\def\@listiv{\leftmargin\leftmarginiv
              \labelwidth\leftmargin
              \advance\labelwidth-\labelsep
              \topsep\z@
              \parsep\baselineskip
              \itemsep\z@}

\fi




%% ALSO FIX PARSEP FOR QUOTES AND LISTS


\if@lsuthesisdoublespace
\fi
%% In double-spacing, bottom of lists should not introduce extra space.
%\def\@endparenv{%
%  \addpenalty\@endparpenalty\@endpetrue}
%% or remove above and instead ensure \topsep and \partopsep are 0?






%% Indent every paragraph even after section heads.
\usepackage{indentfirst}





%% Adjust formatting of various ``\section'' style commands to have a single
%% blank line above and below, and keep them single-spaced.
\if@lsuthesisdoublespace
\renewcommand\section{\@startsection{section}{1}{\z@}%
  {\z@}{.0001\baselineskip}%
  {\normalfont\large\bfseries\singlespacing\addpenalty\@secpenalty\addvspace\@tempskipa}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
  {\z@}{.0001\baselineskip}%
  {\normalfont\large\bfseries\singlespacing\addpenalty\@secpenalty\addvspace\@tempskipa}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
  {\z@}{.0001\baselineskip}%
  {\normalfont\large\bfseries\singlespacing\addpenalty\@secpenalty\addvspace\@tempskipa}}
\else
\renewcommand\section{\@startsection{section}{1}{\z@}%
  {\baselineskip}{\baselineskip}%
  {\normalfont\large\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
  {\baselineskip}{\baselineskip}%
  {\normalfont\large\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
  {\baselineskip}{\baselineskip}%
  {\normalfont\normalsize\bfseries}}
\fi


%% \emergencystretch was added in TeX3 but LaTeX2e sets it to 0. It is
%% used only when a paragraph would have an overfull line, then TeX
%% tries again willing to make other paragraph lines worse to avoid the
%% overfull line.
\setlength\emergencystretch{2em}



\if@lsuthesisraggedright
%% The next two lines are a copy of the LaTeX \raggedright macro without
%% the bit that sets \parindent to 0. But the simple approach of
%% \raggedright bypasses hyphenation and also doesn't carry into certain
%% environments such as footnotes. Thus we instead load a package that
%% addresses those shortcomings.
%\let\\\@centercr\@rightskip\@flushglue \rightskip\@rightskip
%\leftskip\z@skip
\usepackage{ragged2e}
\setlength\RaggedRightParindent\parindent
%\setlength\RaggedRightRightskip{0pt plus 3em} % default is 0pt plus 2em
%% If we didn't increase \emergencystretch above for all documents, then
%% we would at least need to increase \RaggedRightRightskip.
\RaggedRight
\fi


\if@lsuthesissizes
%% We loaded ``book'' with 12pt. Now customize to LSU requirements.
%% Some of this is from ``book.cls'', some from ``bk12.clo''.
%\renewcommand\scriptsize{\@setfontsize\scriptsize\@xpt\@xiipt}
%\let\LARGE=\large\renewcommand\large{\@setfontsize\large\@xiipt{14.5}}
%\let\tiny=\scriptsize\let\Large=\large\let\huge=\LARGE\let\Huge=\LARGE
\let\tiny=\scriptsize
\DeclareRobustCommand\large{\@setfontsize\large\@xiipt{14.5}}
\DeclareRobustCommand\Large{\@setfontsize\Large{14}{17.3}}
\DeclareRobustCommand\LARGE{\@setfontsize\LARGE{16}{20.2}}
\let\huge=\Large
\let\Huge=\Large

\if@lsuthesisdoublespace
%\renewcommand\normalsize{%
%   \@setfontsize\normalsize\@xiipt{14.5}%
%   \abovedisplayskip 3\p@ \@plus3\p@ \@minus3\p@
%   \abovedisplayshortskip \z@ \@plus3\p@ \@minus0\p@
%   \belowdisplayshortskip \abovedisplayskip
%   \belowdisplayskip \abovedisplayskip
%   \abovedisplayskip 3\p@ \@plus3\p@ \@minus3\p@
%   \abovedisplayshortskip \z@ \@plus3\p@ \@minus0\p@
%   \belowdisplayshortskip \abovedisplayskip
%   \belowdisplayskip \abovedisplayskip
%   \let\@listi\@listI}
%\normalsize
%\renewcommand\small{%
%   \@setfontsize\small\@xipt{13.6}%
%   \abovedisplayskip \z@ \@plus3\p@ \@minus3\p@
%   \abovedisplayshortskip \abovedisplayskip
%   \belowdisplayshortskip \abovedisplayskip
%   \def\@listi{\leftmargin\leftmargini
%               \topsep 9\p@ \@plus3\p@ \@minus5\p@
%               \parsep 4.5\p@ \@plus2\p@ \@minus\p@
%               \itemsep \parsep}%
%   \belowdisplayskip \abovedisplayskip
%}
\fi
\fi


%% LSU doesn't want headings. Page number should occur centered in footer
%% on every page (except title page).
\pagestyle{plain}


\renewcommand\contentsname{Table of Contents}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{2}


%% Not that \part is likely to be used in an LSU thesis, but we
%% replace it to conform to our style. The ToC line will have
%% ``Part 3. Title'' instead of ``3  Title''.
\def\@part[#1]#2{%
    \ifnum \c@secnumdepth >-2\relax
      \refstepcounter{part}%
      \addcontentsline{toc}{part}{\partname\space\thepart.\space#1}%
    \else
      \addcontentsline{toc}{part}{#1}%
    \fi
    \markboth{}{}%
    {\centering
     \interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >-2\relax
       \huge\bfseries \partname\space \thepart
       .
     \fi
     \Huge \bfseries #2\par\nobreak
     \if@lsuthesisdoublespace\else\leavevmode\par\nobreak\fi}%
    \@endpart}
\def\@spart#1{%
    {\centering
     \interlinepenalty \@M
     \normalfont
     \Huge \bfseries #1\par\nobreak
     \if@lsuthesisdoublespace\else\leavevmode\par\nobreak\fi}%
    \@endpart}


%% Replacement \@chapter so that the table-of-contents line will
%% have ``Chapter 3. Title'' and ``Appendix B. Title'' instead
%% of ``3  Title'' and ``B  Title''. Furthermore, the list-of-figures
%% and list-of-tables spacing between lines is unrelated to chapter
%% changes.
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
                       \if@mainmatter
                         \refstepcounter{chapter}%
                         \typeout{\@chapapp\space\thechapter.}%
                         \addcontentsline{toc}{chapter}%
                                   {\@chapapp\space\thechapter.\space#1}%
                       \else
                         \addcontentsline{toc}{chapter}{#1}%
                       \fi
                    \else
                      \addcontentsline{toc}{chapter}{#1}%
                    \fi
                    \chaptermark{#1}%
%                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
%                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \if@twocolumn
                      \@topnewpage[\@makechapterhead{#2}]%
                    \else
                      \@makechapterhead{#2}%
                      \@afterheading
                    \fi}


%% Replacement \@makechapterhead and \@makeschapterhead to no longer
%% introduce whitespace at the top of the page, and reduce whitespace below.
%% Also, chapter headings should be ``Chapter X. Title'' rather than
%% ``Chapter X\\Title''.
\def\@makechapterhead#1{%
  %\vspace*{50\p@}%
  {\parindent \z@ \raggedright \normalfont
   \if@lsuthesisdoublespace\singlespacing\fi
    \ifnum \c@secnumdepth >\m@ne
      \if@mainmatter
        \Large\bfseries \@chapapp\space \thechapter
        .
      \fi
    \fi
    \interlinepenalty\@M
    \Large \bfseries #1\par\nobreak
    \if@lsuthesisdoublespace\else\leavevmode\par\nobreak\fi
  }}
\def\@makeschapterhead#1{%
  {\parindent \z@ \raggedright \normalfont
   \if@lsuthesisdoublespace\singlespacing\fi
    \interlinepenalty\@M
    \Large \bfseries #1\par\nobreak
    \if@lsuthesisdoublespace\else\leavevmode\par\nobreak\fi
  }}

%% Replacement \@sect so that section-level and below lines in
%% table-of-contents will have ``2.3. Title'' instead of ``2.3 Title''.
\def\@sect#1#2#3#4#5#6[#7]#8{%
  \ifnum #2>\c@secnumdepth
    \let\@svsec\@empty
  \else
    \refstepcounter{#1}%
    \protected@edef\@svsec{\@seccntformat{#1}\relax}%
  \fi
  \@tempskipa #5\relax
  \ifdim \@tempskipa>\z@
    \begingroup
      #6{%
        \@hangfrom{\hskip #3\relax\@svsec}%
          \interlinepenalty \@M #8\@@par}%
    \endgroup
    \csname #1mark\endcsname{#7}%
    \addcontentsline{toc}{#1}{%
      \ifnum #2>\c@secnumdepth \else
        \protect\numberline{\csname the#1\endcsname.}%
      \fi
      #7}%
  \else
    \def\@svsechd{%
      #6{\hskip #3\relax
      \@svsec #8}%
      \csname #1mark\endcsname{#7}%
      \addcontentsline{toc}{#1}{%
        \ifnum #2>\c@secnumdepth \else
          \protect\numberline{\csname the#1\endcsname.}%
        \fi
        #7}}%
  \fi
  \@xsect{#5}}


%% Change section heads from ``2.1.2   Title'' to ``2.1.2. Title''
\def\@seccntformat#1{\csname the#1\endcsname.\enskip} 

%% Eliminate hanging indentation in section heads
\def\@hangfrom#1{\noindent#1}



%% Replacement \@caption so that the list-of-figures line will
%% have ``Figure 2.3. Caption'' instead of ``2.3  Caption''.
\long\def\@caption#1[#2]#3{%
  \par
  \addcontentsline{\csname ext@#1\endcsname}{#1}%
  %{\csname#1name\endcsname\space\csname the#1\endcsname.\space#2}%
    {\protect\numberline{\csname the#1\endcsname.}{\ignorespaces #2}}%
  \begingroup
    \@parboxrestore
    \if@minipage
      \@setminipage
    \fi
    \normalsize
    \@makecaption{\csname fnum@#1\endcsname}{\ignorespaces #3}\par
  \endgroup}


%% Replacement \@makecaption so that captions will start as
%% ``Figure 2.3. Some caption...'' instead of ``Figure 2.3: Some caption...''
\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{#1. #2}%
  \ifdim \wd\@tempboxa >\hsize
    #1. #2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}


%% Replacement \l@part so that part-level lines in table-of-contents
%% won't use boldface or larger fontsize and will fill with dots.
\renewcommand*\l@part[2]{%
  \ifnum \c@tocdepth >-2\relax
    \addpenalty{-\@highpenalty}%
    \addvspace{2.25em \@plus\p@}%
    \setlength\@tempdima{3em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak
      \leaders\hbox{$\m@th \mkern \@dotsep mu\hbox{.}\mkern \@dotsep mu$}\hfill
      \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}


%% Replacement \l@chapter so that chapter-level lines in table-of-contents
%% won't use boldface and will fill with dots. The \@tempdima value below
%% is used for the hanging indent size as well as by the \numberline
%% macro used for figures and tables.
\renewcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip\baselineskip
    \setlength\@tempdima{2.4em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak
      \leaders\hbox{$\m@th \mkern \@dotsep mu\hbox{.}\mkern \@dotsep mu$}\hfill
      \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}
\let\l@figure\l@chapter
\let\l@table\l@chapter

\renewcommand*\l@section{\@dottedtocline{1}{2.4em}{2.4em}}
\renewcommand*\l@subsection{\@dottedtocline{2}{4.8em}{3.2em}}
\renewcommand*\l@subsubsection{\@dottedtocline{3}{8.0em}{4.0em}}



%% Introduce a negative space at top of table-of-contents to counteract
%% space preceding first toc entry. In double-spacing the chapter head
%% introduces no extra space because normally the following paragraph has
%% a space at the top, but in single-spacing the chapter head introduces
%% an extra space, but then the ToC also introduces another space!
\if@lsuthesisdoublespace\else
\let\@lsu@@starttoc\@starttoc
\def\@starttoc#1{\vskip-\baselineskip
  \@lsu@@starttoc{#1}}
\fi


%% Replacement \titlepage..\endtitlepage so that title page contributes to
%% page numbering (even though page number isn't displayed on that page).
\renewenvironment{titlepage}
    {%
       \cleardoublepage
       \if@twocolumn
         \@restonecoltrue\onecolumn
       \else
         \@restonecolfalse\newpage
       \fi
       \thispagestyle{empty}%
       \setcounter{page}\@ne
    }%
    {\if@restonecol\twocolumn \else \newpage \fi
      \if@twoside\else
%      \setcounter{page}\@ne  %% Commented out for LSU requirement
      \fi
    }


\endinput
%%
%% End of file `lsuthesis.cls'.
