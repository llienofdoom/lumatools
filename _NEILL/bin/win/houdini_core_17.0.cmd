@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\houdini
SET LA_HOU_CURRENT=0001
python houdini_core.py %*
