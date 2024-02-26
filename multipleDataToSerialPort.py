#run this code in micropython https://python.microbit.org/v/3/project
from microbit import *
import utime

# Initialize the UART serial communication
uart.init(baudrate=115200)

while True:
    temp = temperature()  # Use a different variable name
    compass_heading = compass.heading()
    # Create a CSV-formatted string
    data_str = "{},{},{}\n".format(utime.ticks_ms(), temp, compass_heading)
    uart.write(data_str)  # Send data over serial
    utime.sleep(1)  # Delay for 1 second
