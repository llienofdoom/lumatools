CALL la_global.cmd

cd %PYTHONPATH%\ffmpeg
python la_mov2jpg.py %*
