import serial
import time
#This will write 3 values into 3 columns in a CSV file and is related to the file https://github.com/mrroberts-mslt/pythonMicrobitDatabases/blob/main/multipleDataToSerialPort.py
#Mac port
#port = "/dev/cu.usbmodem14602"
port = "COM6"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
while True:
  data = s.readline()
  #CONVERT BYTES TO STRING 
  data = data.decode('utf-8').strip()
  print(data)
  time.sleep(2)
  data = str(data)
  file = open("time_temp_compass.csv", 'a')
  file.write(data + "\n")
  file.close()
