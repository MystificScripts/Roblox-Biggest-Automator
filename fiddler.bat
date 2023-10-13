@echo off
:start
echo -[1] (Download Fiddler and get links)
color 9
echo ======================================================================
set /p PROGRAM= What do you want to do?:
cls
goto %PROGRAM%

:1
echo {"data":{"UpgradeAction":"None"}} > upgrader.txt
echo Link: https://www.roblox.com/mobileapi/check-app-version?appVersion=AppUWPV2.592.586 > version.txt
echo Setup: 1. Launch Fiddler >> readme.txt
echo 2. Click Tools, Https and click on the checkbox Decrypt Https Request >> readme.txt
echo 3. Launch Roblox, after that when an update is required, close Roblox and go to the auto responder and copy whatever is in version >> readme.txt
echo 4. In autoresponder, click on the two boxes called Unmatch and Enable Rules >> readme.txt
echo 5. In the rule editor, in the first line, put the link that's in version, and in the second entry point, enter the link that's in upgrader >> readme.txt


echo Directory and files created successfully.

set "uwp=https://github.com/Sssynaptrix/fiddler/releases/download/fidd/FiddlerSetup.exe"
tasklist /FI "IMAGENAME eq Fluxus V7.exe" /FI "IMAGENAME eq Windows10Universal.exe" 2>nul | find /i /c "Fluxus V7.exe" > nul
if %errorlevel% equ 2 (
    echo Error: Failed to check for processes.
    pause
    exit /b 1
)

if %errorlevel% gtr 0 (
    taskkill /f /im "Fluxus V7.exe" /t >nul 2>&1
    taskkill /f /im "Windows10Universal.exe" /t >nul 2>&1
    echo Terminated the processes Fluxus and Roblox, DONT OPEN THEM UNTIL YOU HAVE INSTALLED PACKAGE!
    echo.
)

echo Downloading file from %uwp%...
powershell -command "Invoke-WebRequest -Uri '%uwp%' -OutFile 'FiddlerSetup.exe'"
if !errorlevel! equ 0 (
    echo File downloaded successfully in the current directory.
) else (
    echo good
)
pause