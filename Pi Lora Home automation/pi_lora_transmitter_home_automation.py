#transmitter
import spidev as SPI
import ST7789#library fot 1.4 tft screen
import RPi.GPIO as GPIO
import serial
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



#GPIO define
RST = 17
DC = 25
BL = 24
bus = 0 
device = 0 


KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16
KEY4_PIN       = 12


# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)
disp.Init()

# Clear display.
disp.clear()

GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY1_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY2_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY3_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY4_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = 240
height = 240
image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


font = ImageFont.truetype(r'/home/pi/Desktop/PCLinuxOSFonts/Arial, Regular.ttf',22)
font1 = ImageFont.truetype(r'/home/pi/Desktop/PCLinuxOSFonts/Arial, Bold.ttf',23)

draw.text((0, 50), 'PRESS KEY1(RELAY1)', fill = "WHITE",font = font)#display text on tft screen
draw.text((0, 90), 'PRESS KEY2(RELAY2)', fill = "WHITE",font = font)
draw.text((0, 130),'PRESS KEY3(RELAY3)', fill = "WHITE",font = font)
draw.text((0, 170),'PRESS KEY4(RELAY4)', fill = "WHITE",font = font)
draw.text((20, 210),'SB COMPONENTS', fill = "YELLOW",font = font1)

lora = serial.Serial(port = '/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)


# try:
while True:
    # with canvas(device) as draw:

    draw.ellipse((0,0,30,30), outline=0, fill="yellow") #display ellips on tft screen
    draw.ellipse((60,0,90,30), outline=0, fill="yellow") 
    draw.ellipse((120,0,150,30), outline=0, fill="yellow") 
    draw.ellipse((180,0,210,30), outline=0, fill="yellow") 
    
        
    if GPIO.input(KEY1_PIN) == GPIO.LOW: # button is released
        draw.ellipse((0,0,30,30), outline=255, fill="yellow") #A button
        lora.write(b'A/n')#send "A" to other lora
        print ("A")
        
    else: # button is pressed:
        draw.ellipse((0,0,30,30), outline=255, fill="red") 

     
    if GPIO.input(KEY2_PIN) == GPIO.LOW: # button is released
        draw.ellipse((60,0,90,30), outline=255, fill="yellow") #B button]
        lora.write(b'B\n')
        print ("B")
        
    else: # button is pressed:
        draw.ellipse((60,0,90,30), outline=255, fill="red")

        
    if GPIO.input(KEY3_PIN) == GPIO.LOW: # button is released
        draw.ellipse((120,0,150,30), outline=255, fill="yellow") #C button
        lora.write(b'C\n')
        print ("C")
        
    else: # button is pressed:
        draw.ellipse((120,0,150,30), outline=255, fill="red") 


    if GPIO.input(KEY4_PIN) == GPIO.LOW: # button is released
        draw.ellipse((180,0,210,30), outline=255, fill="yellow") #D button
        lora.write(b'D\n')
        print ("D")
        
    else: # button is pressed:
        draw.ellipse((180,0,210,30), outline=255, fill="red") 
    disp.ShowImage(image,0,0)
    
    time.sleep(0.2)#delay of 200ms
    

