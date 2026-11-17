@echo off
echo ==============================================
echo   subs4R - Dev Mode (Go + Vite React)
echo ==============================================
echo.
start "subs4R Backend (Port 8080)" cmd /k "cd /d %~dp0..\backend && go run ."
timeout /t 2 >nul
start "subs4R Frontend (Port 5173)" cmd /k "cd /d %~dp0.. && npm run dev"
timeout /t 3 >nul
start http://localhost:5173
