@ECHO OFF
CALL %LA_ROOT%\_%LA_BRANCH%\bin\win\la_global.cmd

cd /d %PYTHONPATH%\houdini
SET LA_HOU_CURRENT=0036
REM SET OCIO=H:\SITE\ocio\aces_1.0.3\config.ocio
python houdini_fx_18-5.py %*
