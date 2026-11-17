@echo off
echo ==============================================
echo   subs4R - Launch Production Server
echo ==============================================
echo.
cd /d "%~dp0..\backend"
if not exist "subs4r-server.exe" (
    echo Building subs4r-server...
    go build -o subs4r-server.exe .
)
echo Starting server on http://localhost:8080
start http://localhost:8080
subs4r-server.exe
pause
