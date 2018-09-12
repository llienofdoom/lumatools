CALL %LA_ROOT%\_%LA_BRANCH%\bin\la_global.cmd

cd /d %PYTHONPATH%\ffmpeg
python la_mov2jpg.py %*
