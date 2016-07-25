@echo off
color a
mode con: cols=20 lines=1
set /p answer=Restart (y/n)?:
if %answer%==y start "" "C:\Users\kevsi\Desktop\gamedir\killre.bat"
if %answer%==n taskkill /IM pythonw.exe /F
set /p answer3=Enter Score (y/n)?:
if %answer3%==y start "" "C:\Users\kevsi\Desktop\gamedir\main\Last Score.py"
if %answe3r%==n taskkill /IM pythonw.exe /F
exit
