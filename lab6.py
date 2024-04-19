import tkinter as tk
from pyfirmata import Arduino, util


class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arduino RGB LED PWM Control")

        # Adjust the padding around the window content
        self.content_frame = tk.Frame(master, padx=250, pady=50)
        self.content_frame.pack(expand=True, fill=tk.BOTH)

        # Connect to Arduino
        ports_to_try = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1']  # List of ports to try
        self.board = None  # Initialize board variable outside the loop
        
        for port in ports_to_try:
            try:
                self.board = Arduino(port)
                print(f"Arduino connected successfully on port: {port}")
                break  # Exit the loop if the Arduino is connected successfully
            except Exception as e:
                print(f"Failed to connect to Arduino on port {port}: {e}")
                print("Trying the next port...")
        
        # Configure pins for PWM output
        self.led_pins = {
            'red': 9,
            'green': 10,
            'blue': 11
"""
            'red': self.board.get_pin('d:9:p'),
            'green': self.board.get_pin('d:10:p'),
            'blue': self.board.get_pin('d:11:p')
            """
            ###write your code here###
            ##hint: configure the pins for PWM output(digital pins 9, 10, 11)

        }

        self.pwm_values = {'red': 0, 'green': 0, 'blue': 0}  # PWM value range from 0 to 255
        self.running = True

        # PWM control sliders for each LED
        for color in ['red', 'green', 'blue']:
            setattr(self, f"{color}_slider", tk.Scale(self.content_frame, from_=0, to=255, orient=tk.HORIZONTAL, label=f"{color.capitalize()} PWM", command=lambda value, c=color: self.update_pwm(c, value)))
            getattr(self, f"{color}_slider").pack(padx=20, pady=10)

    def update_pwm(self, color, value):
        
        self.pwm_values[color] = int(value)
        '''if self.pwm_values[color] > 0:
            self.led_pins[color].write(1)  # LED ON
            time.sleep(int(value)/ 1000.0)  # Adjust on time based on PWM value
        
        if self.pwm_values[color] < 100:
            self.led_pins[color].write(0)  # LED OFF
            time.sleep((100 - int(value)) / 1000.0)  # Adjust off time based on PWM value
'''
        #self.pwm_values[color] = int(value)  # Update PWM value for the specified color
        #self.board.digital[self.led_pins[color]].write(self.pwm_values[color])  # Write PWM value to the corresponding pin
        self.led_pins[color].write(self.pwm_values[color] / 255.0)
    
    def close(self):
        self.running = False
        self.board.exit()
        self.master.destroy()

# Create the GUI window
root = tk.Tk()
app = ArduinoGUI(root)

# Ensure the application cleans up properly upon exit
root.protocol("WM_DELETE_WINDOW", app.close)

# Run the application
root.mainloop()
