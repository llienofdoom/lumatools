@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\discord
python discord_houdiniProdVersionCheck.py %*
