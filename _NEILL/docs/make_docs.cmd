@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %LA_ROOT%\_%LA_BRANCH%\docs\src

H:\_distros\_lumatools\latex\miktex\texmfs\install\miktex\bin\pdflatex.exe -quiet -aux-directory=.\tmp -output-directory=.. -job-name=lumatools _main.tex
