@echo off
SET SERVICE_NAME=DotnetPrintService
SET DOTNET_EXE_PATH="C:\Program Files\dotnet\dotnet.exe"
SET PROJECT_DLL_PATH=%~dp0bin\Debug\net6.0\print-service-dotnet.dll"
SET NSSM_PATH="C:\Program Files\nssm\nssm.exe"

IF NOT EXIST %NSSM_PATH% (
    echo NSSM no está instalado.
    pause
    exit /b
)

IF NOT EXIST %DOTNET_EXE_PATH% (
    echo No se encontró dotnet.exe.
    pause
    exit /b
)

%NSSM_PATH% install %SERVICE_NAME% %DOTNET_EXE_PATH% "%PROJECT_DLL_PATH%"
%NSSM_PATH% set %SERVICE_NAME% DisplayName "Servicio de Impresión PostScript .NET"
%NSSM_PATH% set %SERVICE_NAME% Start SERVICE_AUTO_START
pause