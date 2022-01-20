#RECEIVER
import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(33,GPIO.OUT)#relay connected to pin 33
GPIO.setup(35,GPIO.OUT)#relay connected to pin 35
GPIO.setup(37,GPIO.OUT)#relay connected to pin 37
GPIO.setup(40,GPIO.OUT)#relay connected to pin 40

#initially these pin are low
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)
GPIO.output(40,GPIO.LOW)

request1 = 0;#variables
flag_1=0;

request2 = 0;
flag_2=0;

request3 = 0;
flag_3=0;

request4 = 0;
flag_4=0;

#serial interface
lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

try:
    while 1:
        data_Read = lora.readline(1)#read data comming from other pi lora Hat 
        if data_Read is not None and b'A' in data_Read:
          #ones, turn led on!
          if flag_1 == 0:
            print("relay 1 on")
            GPIO.output(33,GPIO.HIGH)
            flag_1=1; #change flag variable
            
            
          #twice, turn led off!
          elif flag_1 == 1:
            print("relay 1 off")
            GPIO.output(33,GPIO.LOW)
            flag_1=0; #change flag variable again
            
            
        if data_Read is not None and b'B' in data_Read:
          #ones, turn led on!
          if flag_2 == 0:
            print("relay 2 on")
            GPIO.output(35,GPIO.HIGH)
            flag_2=1; #change flag variable
            
          #twice, turn led off!
          elif flag_2 == 1:
            print("relay 2 off")
            GPIO.output(35,GPIO.LOW)
            flag_2=0; #change flag variable again
            
            
        if data_Read is not None and b'C' in data_Read:
          #ones, turn led on!
          if flag_3 == 0:
            print("relay 3 on")
            GPIO.output(37,GPIO.HIGH)
            flag_3=1; #change flag variable
            
          #twice, turn led off!
          elif flag_3 == 1:
            print("relay 3 off")
            GPIO.output(37,GPIO.LOW)
            flag_3=0; #change flag variable again

        if data_Read is not None and b'D' in data_Read:
          #ones, turn led on!
          if flag_4 == 0:
            print("relay 3 on")
            GPIO.output(40,GPIO.HIGH)
            flag_4=1; #change flag variable
            
          #twice, turn led off!
          elif flag_4 == 1:
            print("relay 3 off")
            GPIO.output(40,GPIO.LOW)
            flag_4=0; #change flag variable again
            
        time.sleep(0.2)#wait for 200ms
        
except KeyboardInterrupt:
    GPIO.cleanup()
