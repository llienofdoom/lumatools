@ECHO OFF
CALL H:\_distros\_lumatools\lumatools\_NEILL\bin\win\la_global.cmd

cd /d H:\_distros\_lumatools\lumatools\_NEILL\src\nuke\golf
H:\_distros\_lumatools\la_venv_2018-09-01\Scripts\python golf_convert.py %*
