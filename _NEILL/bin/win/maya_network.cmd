@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\maya
REM SET LA_HOU_CURRENT=0035
REM SET OCIO=H:\SITE\ocio\aces_1.2\config.ocio
python maya_network.py %*
