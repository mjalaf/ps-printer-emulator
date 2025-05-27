@echo off
SET SERVICE_NAME=PrintServiceNode
SET NSSM_PATH="C:\Program Files\nssm\nssm.exe"

IF NOT EXIST %NSSM_PATH% (
    echo NSSM no está instalado en "C:\Program Files\nssm\nssm.exe"
    pause
    exit /b
)

net stop %SERVICE_NAME%
%NSSM_PATH% remove %SERVICE_NAME% confirm
pause