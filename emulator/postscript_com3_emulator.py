import serial
import os
import datetime

PORT = 'COM6'  # <-- Emulador escucha aquí (conectado virtualmente a COM5)
BAUD_RATE = 9600
OUTPUT_DIR = 'impresiones'

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_filename():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(OUTPUT_DIR, f"impresion_{timestamp}.ps")

def main():
    ensure_output_dir()
    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Escuchando en {PORT}... (presiona Ctrl+C para salir)")
            buffer = ""
            while True:
                data = ser.read(1024).decode("utf-8", errors="replace")
                if data:
                    print(f"Recibido: {data}")
                    buffer += data
                    if "showpage" in buffer:
                        filename = generate_filename()
                        with open(filename, "w", encoding="utf-8") as f:
                            f.write(buffer)
                        print(f"Guardado: {filename}")
                        buffer = ""
    except serial.SerialException as e:
        print(f"No se pudo abrir {PORT}. Error: {e}")
    except KeyboardInterrupt:
        print("\nEmulador detenido.")

if __name__ == '__main__':
    main()
