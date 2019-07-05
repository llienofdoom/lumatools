@ECHO OFF

set LA_ROOT=H:\_distros\_lumatools\lumatools
set LA_VENV=H:\_distros\_lumatools\la_venv_2018-09-01
set LA_BRANCH=NEILL

CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\houdini
python houdini_hython.py H:\SITE\houdini17.5\hrender.py %*
