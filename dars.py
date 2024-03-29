import tkinter as tk
import time
import serial

class GasMonitor:
    def __init__(self, master):
        self.master = master
        master.title("Gas Monitor")

        # Create a label to display the current gas level
        self.gas_label = tk.Label(master, text="Gas Level: 0%")
        self.gas_label.pack()

        # Open the serial port
        self.ser = serial.Serial('COM1', 9600, timeout=1)

        # Create a function to read the gas level from the gas detector
        self.read_gas_level()

    def read_gas_level(self):
        # Read the gas level from the gas detector
        line = self.ser.readline().decode('utf-8').strip()
        gas_level = int(line)

        # Update the label to display the current gas level
        self.gas_label.config(text=f"Gas Level: {gas_level}%")

        # Schedule the next reading
        self.master.after(1000, self.read_gas_level)

if __name__ == "__main__":
    root = tk.Tk()
    monitor = GasMonitor(root)
    root.mainloop()
