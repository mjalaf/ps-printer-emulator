# Emulador de Impresora PostScript (Puerto COM)

Este emulador simula una impresora PostScript conectada a un puerto COM. Su objetivo es permitir el desarrollo y prueba de sistemas que imprimen a través de puertos seriales sin requerir hardware físico.

---

## 🔌 Configuración de Puertos

Para simular correctamente una impresora conectada a un puerto COM, utilizamos la herramienta **[com0com](https://sourceforge.net/projects/com0com/)** para crear un par de puertos virtuales.

### ✅ Recomendación

Crear un par virtual así:

```
COM5 <--> COM6
```

### Flujo esperado:

| Componente        | Puerto utilizado |
|-------------------|------------------|
| API Node.js       | COM5             |
| Emulador Python   | COM6             |

1. La API escribe en `COM5`.
2. com0com transfiere automáticamente los datos a `COM6`.
3. El emulador escucha en `COM6` y guarda los datos recibidos en archivos `.ps`.

---

## 📥 Formato de Entrada (Impresiones)

El emulador está diseñado para recibir contenido en formato **PostScript (PS)**. Esto es importante porque **una impresora PostScript real no imprimirá nada si el contenido no es válido**.

### Ejemplo válido (texto simple)

```postscript
%!PS
/Texto (Hola Tincho!) def
72 500 moveto
Texto show
showpage
```

- `%!PS`: encabezado requerido para identificar el archivo como PostScript.
- `showpage`: **obligatorio** para indicar el final del trabajo de impresión.
- Sin `showpage`, **una impresora PostScript no imprimirá nada**.

### Características del lenguaje PostScript:

- Es un lenguaje de descripción de páginas.
- Define coordenadas, texto, líneas, figuras, fuentes, etc.
- Todo debe terminar con `showpage` para "enviar al papel".

---

## 🖨️ ¿Qué hace el emulador?

- Escucha en `COM6` a 9600 baudios.
- Acumula el contenido recibido.
- Cuando detecta la palabra clave `showpage`, guarda todo el contenido en un archivo `.ps` en la carpeta `impresiones/`.
- El archivo puede visualizarse con herramientas como **Ghostscript**, GSView o convertirse a PDF.

---

### Ver como PDF

```bash
gswin64c -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=salida.pdf impresion_xxx.ps
```

---

## 🧹 Limpieza

Todos los archivos generados se guardan en la carpeta `impresiones/`. Podés automatizar su limpieza o conversión posterior si lo necesitás.

---

## ✅ Requisitos para probar

- Python 3
- pyserial (`pip install pyserial`)
- com0com configurado
- Un backend que envíe contenido PS por COM (ej. `print-service-node`)

---

## 👨‍💻 Autor

Desarrollado por Martín Jalaf como parte de un sistema de prueba de impresión serial PostScript.