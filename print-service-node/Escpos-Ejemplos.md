# 💳 ESC/POS Print Examples via cURL

This file provides example cURL commands to send ESC/POS-formatted data to the backend (Node.js or .NET), which will then relay the data to the serial printer.

---

## ⚙️ How to send

Make sure your printer (or emulator) is listening on the corresponding COM port (e.g., COM6). These examples send binary ESC/POS commands as part of the print job.

```bash
curl -X POST http://localhost:3000/print \
  -H "Content-Type: text/plain" \
  --data-binary "<ESC/POS COMMANDS>"
```

---

## 🧾 Simple Receipt

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40Hello!\n\x1d\x56\x41\x10'
```

- `\x1b\x40` → Reset
- `\x1d\x56\x41\x10` → Partial cut

---

## 🧾 Bold Text + Cut

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40\x1b\x45\x01Bold line\n\x1b\x45\x00Normal line\n\x1d\x56\x41\x10'
```

- `\x1b\x45\x01` → Bold ON
- `\x1b\x45\x00` → Bold OFF

---

## 🧾 Centered + Double Width

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40\x1b\x61\x01\x1b\x21\x20TOTAL: €12.50\n\x1b\x21\x00\x1d\x56\x41\x10'
```

- `\x1b\x61\x01` → Center alignment
- `\x1b\x21\x20` → Double width font
- `\x1b\x21\x00` → Normal font

---

## 🧾 With QR Code

```bash
curl -X POST http://localhost:3000/print -H "Content-Type: text/plain" --data-binary $'\x1b\x40\x1d\x28\x6b\x03\x00\x31\x43\x06\x1d\x28\x6b\x03\x00\x31\x45\x30\x1d\x28\x6b\x0f\x00\x31\x50\x30https://tincho.ai\x1d\x28\x6b\x03\x00\x31\x51\x30\x1d\x56\x41\x10'
```

This prints a QR code for `https://tincho.ai`.

---

## 📝 Notes

- You may need to escape the `\x` sequences depending on your shell (`$'...'` works in Bash).
- These examples assume the backend writes to a serial port like COM5, connected virtually to an emulator on COM6.
- Each job ends with `\x1d\x56\x41` (cut paper), used by the emulator to detect print completion.