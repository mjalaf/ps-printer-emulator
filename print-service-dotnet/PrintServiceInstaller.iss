[Setup]
AppName=Servicio Impresora PostScript
AppVersion=1.0
DefaultDirName={pf}\PrintServiceDotnet
OutputBaseFilename=PrintServiceInstaller
OutputDir=.
Compression=lzma
SolidCompression=yes

[Files]
Source: "bin\Debug\net6.0\*"; DestDir: "{app}\bin"; Flags: recursesubdirs
Source: "install_service.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "uninstall_service.bat"; DestDir: "{app}"; Flags: ignoreversion

[Run]
Filename: "{app}\install_service.bat"; StatusMsg: "Instalando el servicio..."; Flags: runhidden

[UninstallRun]
Filename: "{app}\uninstall_service.bat"; StatusMsg: "Desinstalando el servicio..."; Flags: runhidden