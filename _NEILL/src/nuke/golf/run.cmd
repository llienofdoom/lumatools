@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\nuke\golf
rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_fairway.py
rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_reaction.py
H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_putt.py
