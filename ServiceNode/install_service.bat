@echo off
SET SERVICE_NAME=PrintServiceNode
SET EXE_PATH=%~dp0print-service-node.exe
SET NSSM_PATH="C:\Program Files\nssm\nssm.exe"

IF NOT EXIST %NSSM_PATH% (
    echo NSSM no está instalado en "C:\Program Files\nssm\nssm.exe"
    pause
    exit /b
)

%NSSM_PATH% install %SERVICE_NAME% %EXE_PATH%
%NSSM_PATH% set %SERVICE_NAME% DisplayName "Servicio de Impresión PostScript Local"
%NSSM_PATH% set %SERVICE_NAME% Start SERVICE_AUTO_START
pause