import tkinter as tk
from pyfirmata import Arduino, util
import threading
import time

class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arduino LED PWM Control")

        # Adjust the padding around the window content
        self.content_frame = tk.Frame(master, padx=250, pady=50)
        self.content_frame.pack(expand=True, fill=tk.BOTH)

        # Connect to Arduino
        self.board = Arduino('/dev/ttyACM0')  # Adjust your Arduino connection port
        self.led_pin = self.board.get_pin('d:13:o')  # d for digital, 13 for pin, o for output

        self.pwm_value = 0  # PWM value range from 0 to 100
        self.running = True

        # PWM control slider with padding around it
        self.pwm_slider = tk.Scale(self.content_frame, from_=0, to=100, orient=tk.HORIZONTAL, label="PWM", command=self.update_pwm)
        self.pwm_slider.pack(padx=200, pady=10)

    def update_pwm(self, event):
        self.pwm_value = self.pwm_slider.get()

    def simulate_pwm(self):
        while self.running:
            if self.pwm_value > 0:
                self.led_pin.write(1)  # LED ON
                time.sleep(self.pwm_value / 1000.0)  # Adjust on time based on PWM value
            if self.pwm_value < 100:
                self.led_pin.write(0)  # LED OFF
                time.sleep((100 - self.pwm_value) / 1000.0)  # Adjust off time based on PWM value

    def start_pwm_simulation(self):
        self.pwm_thread = threading.Thread(target=self.simulate_pwm)
        self.pwm_thread.daemon = True
        self.pwm_thread.start()

    def close(self):
        self.running = False
        self.pwm_thread.join()
        self.board.exit()
        self.master.destroy()

# Create the GUI window
root = tk.Tk()
app = ArduinoGUI(root)
app.start_pwm_simulation()

# Ensure the application cleans up properly upon exit
root.protocol("WM_DELETE_WINDOW", app.close)

# Run the application
root.mainloop()
