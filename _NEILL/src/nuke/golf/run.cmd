@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\nuke\golf

rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_01_fairway.py
rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_02_approach.py
rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_03_reaction_fairway.py
rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_04_putt.py
rem H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_05_result.py
    H:\_distros\Nuke11.2v4\Nuke11.2.exe -t comp_06_reaction_putt.py
pause
