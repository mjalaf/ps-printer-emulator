# Print Service (PostScript over COM)

Este proyecto permite exponer una API local para enviar datos en formato PostScript a una impresora conectada al puerto COM (como COM3 o COM4), desde una aplicación web (por ejemplo, Angular).

Incluye dos implementaciones:
- **Node.js**
- **.NET 6 (WebAPI)**

También incluye:
- Emulador de impresora en Python (para pruebas sin hardware)
- Scripts para instalación del servicio como servicio de Windows usando NSSM
- Script Inno Setup para generar instalador `.exe`

---

## 📦 Estructura del Proyecto

```
print-service-node/       --> Servicio en Node.js
print-service-dotnet/     --> Servicio en .NET
emulador/                 --> Emulador de impresora en Python
```

---

## ⚙️ Requisitos

### Para Node.js
- Node.js
- `pkg` (`npm install -g pkg`)
- NSSM instalado en: `C:\Program Files\nssm\nssm.exe`

### Para .NET
- .NET 6 SDK
- NSSM
- (Opcional) Inno Setup para crear instalador `.exe`

---

## 🚀 Instalación

### Node.js

```bash
cd print-service-node
npm install
pkg .
```

Para instalar como servicio:

```bash
install_service.bat
```

---

### .NET

```bash
cd print-service-dotnet
dotnet build
```

Luego:

```bash
install_service.bat
```

---

## 🖨️ Emulador de Impresora (Python)

```bash
pip install pyserial
python postscript_com4_emulator_by_job.py
```

Escucha en COM4 y genera un `.txt` por impresión recibida.

---

## 🧪 Diagramas de Secuencia

### Node.js

```mermaid
sequenceDiagram
    participant Browser
    participant NodeService
    participant Impresora

    Browser->>NodeService: POST /print (contenido PostScript)
    NodeService->>Impresora: Enviar datos al puerto COM3
    Impresora-->>NodeService: Confirmación (opcional)
    NodeService-->>Browser: Respuesta HTTP (OK / Error)
```

### .NET

```mermaid
sequenceDiagram
    participant Browser
    participant DotNetService
    participant Impresora

    Browser->>DotNetService: POST /api/print (contenido PostScript)
    DotNetService->>Impresora: Escribir en COM3 vía SerialPort
    Impresora-->>DotNetService: Confirmación (opcional)
    DotNetService-->>Browser: Respuesta HTTP (OK / Error)
```

---

## 📦 Crear Instalador `.exe` con Inno Setup (.NET)

1. Instalar [Inno Setup](https://jrsoftware.org/isinfo.php)
2. Abrir `PrintServiceInstaller.iss` en Inno
3. Compilar

---

## 🧹 Desinstalación

Ambas versiones tienen su propio `uninstall_service.bat` para detener y eliminar el servicio.

---

## 📝 Licencia

MIT