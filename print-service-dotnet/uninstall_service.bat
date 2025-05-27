@echo off
SET SERVICE_NAME=DotnetPrintService
SET NSSM_PATH="C:\Program Files\nssm\nssm.exe"

IF NOT EXIST %NSSM_PATH% (
    echo NSSM no está instalado.
    pause
    exit /b
)

net stop %SERVICE_NAME%
%NSSM_PATH% remove %SERVICE_NAME% confirm
pause