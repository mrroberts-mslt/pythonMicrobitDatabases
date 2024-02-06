import serial, time
port = "COM8"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
while True:
   data = s.readline()
   data = int(data[0:4])
   time.sleep(1)
   data = str(data)
   file = open("temperatures2.csv", 'a')
   file.write(data+",")
   file.close()
