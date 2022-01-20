#Transmitter

import time
import serial

lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

while True:
    n = input("Enter The Message = ")#input the string
    b = bytes(n,'utf-8')#convert string into bytes
    s = lora.write(b)#send the data to other lora
    time.sleep(0.2)#delay of 200ms
