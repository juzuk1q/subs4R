@echo off
echo ==============================================
echo   SubDB Dev Mode (Go Backend + Vite Dev)
echo ==============================================
echo.
start "SubDB Go Backend (Port 8080)" cmd /k "cd /d %~dp0backend && go run ."
timeout /t 2 >nul
start "SubDB Vite React (Port 5173)" cmd /k "cd /d %~dp0 && npm run dev"
timeout /t 3 >nul
start http://localhost:5173
echo Серверы запущены!
