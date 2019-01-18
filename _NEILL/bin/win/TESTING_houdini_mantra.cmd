@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\houdini
rem SET LA_HOU_CURRENT=0011
python houdini_mantra.py %*
