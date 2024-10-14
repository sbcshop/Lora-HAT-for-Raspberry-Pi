#receiver
import serial
import time

# Uncomment suitable line for your Pi and comment other which is not required 
'''For Raspberry Pi 4 & 3'''
lora = serial.Serial(port = '/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)

'''For Raspberry Pi 5'''
#lora = serial.Serial(port = '/dev/ttyAMA0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
 

while True:
    data_read = lora.readline()#read data from other lora
    data = data_read.decode("utf-8")#convert byte into string
    print(data)

        
