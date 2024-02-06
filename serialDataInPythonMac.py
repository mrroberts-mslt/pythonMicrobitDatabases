#ser = serial.Serial('/dev/cu.usbmodem1d12')
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
    ##        data = str(data[0:4])
    print(data)
    record = {"Temp" : data}
    myDB.post('/temp/', record)
    time.sleep(1)


