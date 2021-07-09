import serial
from time import sleep
from serial import Serial

ser = serial.Serial("/dev/ttyS0",38400)

while True:
    ser.write(b'1')
    
    rd=ser.read().decode('utf-8')
    sleep(1)
    dl=ser.inWaiting()
    rd+=ser.read(dl)
    print(rd)
    
    
    
    
