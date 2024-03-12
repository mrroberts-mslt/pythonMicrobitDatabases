import serial
import time
import csv
#This will write 3 values into 3 columns in a CSV file and is related to the file https://github.com/mrroberts-mslt/pythonMicrobitDatabases/blob/main/multipleDataToSerialPort.py
#Mac port
#port = "/dev/cu.usbmodem14602"
port = "COM7"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
while True:
  data = s.readline()
  #CONVERT BYTES TO STRING 
  data = data.decode('utf-8').strip()
  print(data)
  manually_entered_data = input("Enter data: ")
  time.sleep(2)
  data = str(data)
  file = open("elliot.csv", 'a')
  file.write(data + manually_entered_data + "\n")
  file.close()
