# pythonMicrobitDatabases
Sending microbit data via the serial port to a firebase database
Writing Microbit data to a database

Write a forever loop using the micropython editor and flash it to your Microbit.
https://python.microbit.org/v/2 

<i>from microbit import *<br>
while True:<br>
   print(temperature())<br>
   sleep(1000)<br>
   </i>
 
Keep the microbit plugged in to the USB port
The print statement will write to the serial port when the microbit is  plugged in.

Next check which serial port the microbit is using - 
open Terminal / cmd 
python -m serial.tools.list_ports or try python3 -m serial.tools.list_ports

OR
Plug in the micro:bit and open a new terminal window. 
Type ls /dev/cu.* to get a list of connected serial devices; one of them will look like /dev/cu.usbmodem1422 (the exact number depends on your computer).
Type screen /dev/cu.usbmodem1422 115200, replacing the 'usbmodem' number with the number you found in the previous step. 115200 is the baud rate. This will open the micro:bit's serial output and show all messages received from the device. 
To exit, press Ctrl-A then Ctrl-D.

The baud rate is the rate at which information is transferred in a communication channel. Baud rate is commonly used when discussing electronics that use serial communication. In the serial port context, "9600 baud" means that the serial port is capable of transferring a maximum of 9600 bits per second.
Next  - Install pyserial
pip install pyserial
Python “read serial port data” code.
Switch to Thonny or Idle. This code will read whatever is being sent to the serial port. Note the data[0:4] is a substring as the full string includes unwanted chars. The sleep function pauses every second.
import serial, time
port = "/dev/cu.usbmodem1d12"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
while True:
   data = s.readline()
   data = int(data[0:4])
   print(data)
   time.sleep(1)

Run the script - you may need to unplug / plugin the microbit if there is a read error.

Next we will write our serial data to firebase 
For firebase to work you need to use Python 3.6 - I have done this project in MongoDB too which is is better IMHO and works on the latest versions of Python
In Thonny change the Tools > Options > Interpreter or just use Idle on Python 3.6



The code now looks like this:

from firebase import firebase
import serial, time
myDB = firebase.FirebaseApplication("https://temp-6b71e-default-rtdb.europe-west1.firebasedatabase.app/", None)
port = "/dev/cu.usbmodem1d12"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
while True:
   data = s.readline()
   data = int(data[0:4])
   print(data)
   record = {"Temp" : data}
   myDB.post('/temp/', record)
   time.sleep(1)


Sending data from an external microbit to another microbit that is connected to your PC, then send that data to firebase.



Sending Microbit code (accelerometer example)
note the radio.send() sends it as a string - can cause issues.

from microbit import *
import radio
radio.config(group=23)
radio.on()
while True:
   if button_a.was_pressed():
       reading = accelerometer.get_x()
   #reading = temperature()
       display.show(reading)
       radio.send(str(reading))

Receiving Microbit code
#the pass statement is cool because if the value at the port is none then we dont want to send that data

from microbit import *
import radio
radio.config(group=23)
radio.on()
while True:
   message = radio.receive()
   if message is None:
       pass
   else:
       print(message)

Instructions
Plugin the Receiving microbit into the USB port
Plugin a battery pack into the Sending Microbit
Run the python read serial port code in Thonny and press button A on the sending Microbit
Check your shell and check the firebase DB!
You could edit the send code by using other triggers / conditionals on the if statement.

More reading
https://support.microbit.org/support/solutions/articles/19000022103-outputing-serial-data-from-the-micro-bit-to-a-computer
https://bigl.es/friday-fun-sending-serial-data-from-micro-bit-to-laptop/ 
Keiths Firebase vids
https://www.curriculumonline.ie/Senior-cycle/Senior-Cycle-Subjects/Computer-Science/CS-Support-for-Teaching-and-Learning/Support-Material-for-Teaching-and-Learning/2-ALT-Resources/CSinP-ALT/Tutorials-for-Firebase/ 

