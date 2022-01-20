#receiver
import spidev as SPI
import ST7789#tft screen library 1.3 inch display
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


# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)
disp.Init()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = 240
height = 240
image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'/home/pi/Desktop/PCLinuxOSFonts/Arial, Regular.ttf',22)
font1 = ImageFont.truetype(r'/home/pi/Desktop/PCLinuxOSFonts/Arial, Bold.ttf',23)
font2 = ImageFont.truetype(r'/home/pi/Desktop/PCLinuxOSFonts/Arial, Regular.ttf',22)

draw.text((60, 30),'RECEIVER', fill = "WHITE",font = font)#text display on lcd screen
draw.text((20, 0),'SB COMPONENTS', fill = "YELLOW",font = font1)

lora = serial.Serial(port = '/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
disp.ShowImage(image,0,0)
    

while True:
    data_read = lora.readline()#read data from other lora
    
    
    s = data_read.decode("utf-8")#convert byte into string
    #if data_read is not None :
    if s:
        print(data_read)
        draw.text((20,80),s,fill = "YELLOW",font = font2)#display the data on lcd screen
        disp.ShowImage(image,0,0)
        
