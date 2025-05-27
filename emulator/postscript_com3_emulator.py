import serial
import os
import datetime

PORT = 'COM3'  # Puerto virtual de lectura
BAUD_RATE = 9600
OUTPUT_DIR = 'impresiones'

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_filename():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(OUTPUT_DIR, f"impresion_{timestamp}.txt")

def main():
    ensure_output_dir()
    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Escuchando en {PORT}... (presiona Ctrl+C para salir)")
            buffer = ""
            while True:
                if ser.in_waiting:
                    data = ser.read(ser.in_waiting).decode('utf-8', errors='replace')
                    buffer += data
                    if "\n" in buffer or "\x0C" in buffer:  # newline o form feed = fin de trabajo
                        filename = generate_filename()
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(buffer)
                        print(f"Guardado: {filename}")
                        buffer = ""
    except serial.SerialException as e:
        print(f"No se pudo abrir {PORT}. Error: {e}")
    except KeyboardInterrupt:
        print("\nEmulador detenido.")

if __name__ == '__main__':
    main()