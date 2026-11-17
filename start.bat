@echo off
echo ==============================================
echo   Запуск SubDB (Go Backend + React SPA)
echo ==============================================
echo.
cd /d "%~dp0backend"
if not exist "subdb-server.exe" (
    echo Компиляция сервера Go...
    go build -o subdb-server.exe .
)
echo Запуск сервера на http://localhost:8080
start http://localhost:8080
subdb-server.exe
pause
