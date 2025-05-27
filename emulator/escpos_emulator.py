import serial
import os
import datetime
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading

PORT = 'COM6'
BAUDRATE = 9600
OUTPUT_DIR = 'escpos_gui_output'

COMMANDS = {
    b'\x1b\x40': '[RESET]',
    b'\x1b\x61\x00': '[LEFT]',
    b'\x1b\x61\x01': '[CENTER]',
    b'\x1b\x61\x02': '[RIGHT]',
    b'\x1b\x45\x01': '[BOLD ON]',
    b'\x1b\x45\x00': '[BOLD OFF]',
    b'\x1b\x21\x20': '[DOUBLE WIDTH]',
    b'\x1b\x21\x00': '[NORMAL FONT]',
    b'\x1d\x28\x6b': '[QR]',
    b'\x1d\x76': '[GRAPHIC IMAGE]',
    b'\x1d\x56': '[CUT PAPER]',
}

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_filename(suffix):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(OUTPUT_DIR, f"ticket_{timestamp}.{suffix}")

def decode_ticket(data):
    output = []
    i = 0
    while i < len(data):
        matched = False
        for cmd, label in COMMANDS.items():
            if data[i:i+len(cmd)] == cmd:
                output.append(label)
                i += len(cmd)
                matched = True
                break
        if not matched:
            ch = data[i]
            if 32 <= ch <= 126:
                output.append(chr(ch))
            elif ch in (10, 13):
                output.append('\n')
            else:
                output.append('.')
            i += 1
    return ''.join(output)

class EscposGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ESC/POS Ticket Viewer")
        self.text = ScrolledText(root, width=60, height=30, font=("Courier", 10))
        self.text.pack(padx=10, pady=10)
        self.text.insert(tk.END, "Listening on COM6...\n")
        ensure_output_dir()
        self.start_listener()

    def start_listener(self):
        thread = threading.Thread(target=self.listen_serial, daemon=True)
        thread.start()

    def listen_serial(self):
        try:
            with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
                buffer = b""
                while True:
                    data = ser.read(1024)
                    if data:
                        buffer += data
                        if b'\x1d\x56' in buffer:  # CUT PAPER
                            ticket = decode_ticket(buffer)
                            self.text.insert(tk.END, f"\n===== TICKET =====\n{ticket}\n===================\n")
                            self.text.see(tk.END)

                            txt_filename = generate_filename("txt")
                            bin_filename = generate_filename("bin")

                            with open(txt_filename, "w", encoding="utf-8") as f:
                                f.write(ticket)
                            with open(bin_filename, "wb") as f:
                                f.write(buffer)

                            print(f"Ticket saved: {txt_filename}, {bin_filename}")
                            buffer = b""
        except serial.SerialException as e:
            self.text.insert(tk.END, f"\nError opening {PORT}: {e}\n")
            self.text.see(tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = EscposGUI(root)
    root.mainloop()