#receiver
import serial
import time

lora = serial.Serial(port = '/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)

while True:
    data_read = lora.readline()#read data from other lora
    data = data_read.decode("utf-8")#convert byte into string
    print(data)

        
