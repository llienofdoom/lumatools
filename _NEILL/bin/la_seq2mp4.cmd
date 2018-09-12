CALL la_global.cmd

cd %PYTHONPATH%\ffmpeg
python la_seq2mp4.py %*
