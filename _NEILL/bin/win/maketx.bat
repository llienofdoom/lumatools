 @echo off
echo TX:Convertor version Bata0.01
for %%f in (%*) do (
echo original file %%f convert to %%~dpnf.tx
H:\_distros\htoa-5.1.1_r126b954_houdini-18.0.391\htoa-5.1.1_r126b954_houdini-18.0.391\scripts\bin\maketx.exe -v -u --oiio --checknan --filter lanczos3 %%f -o %%~dpnf.tx
)
echo TX-Convertor DONE.
pause;