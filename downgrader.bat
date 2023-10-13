@echo off
setlocal enabledelayedexpansion
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrative privileges. Please run it as an administrator.
    pause
    exit /b 1
)

:start
echo -[1] (Downgrade Roblox so you can bypass UWP hyperion/byfron!)
color 9
echo ======================================================================
set /p PROGRAM= What do you want to do?:
cls
goto %PROGRAM%

:1
set "uwp=https://github.com/cerealwithmilk/uwp/releases/download/2.592.586.0/RobloxUWP-2.592.586.0-cerealwithmilk.Msixbundle"
set "put=C:\Windows\IME\Roblox.msixbundle"

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
powershell -command "Invoke-WebRequest -Uri '%uwp%' -OutFile '%put%'"
if !errorlevel! equ 0 (
    echo File downloaded successfully.
    echo Opening the downloaded file...
    start "" "%put%"
) else (
    echo Error: Failed to download the file.
)
pause
