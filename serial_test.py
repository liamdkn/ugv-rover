import serial 
import time

ser = serial.Serial('/dev/serial0', 115200)

some_string = '{"T":1,"L":0.1,"R":0.1}'
stop_string = '{"T":1,"L":0,"R":0}'


for i in range(20):
    time.sleep(2)
    ser.write(some_string.encode() + b'\n')
    data = ser.readline().decode('utf-8')
    if data:
        print(f"Received: {data}", end='')
ser.write(stop_string.encode() + b'\n')