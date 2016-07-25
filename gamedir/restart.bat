@echo off
color a
mode con: cols=160 lines=1
set /p answer=Restart (y/n)?:
if %answer%==y start "" "C:\Users\kevsi\Desktop\gamedir\killre.bat"
pause
