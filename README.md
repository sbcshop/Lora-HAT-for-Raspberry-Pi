# Lora-HAT-for-Raspberry-Pi
Pi LoRa™ Lora Hat is a low-power consumption data transmission board, comes with an onboard CH340 USB TO UART converter, Voltage Level Translator(74HC125V), E22-900T22S/E22-400T22S SMA antenna connector that covers 868MHz/433MHz frequency band ,IPEX antenna connector, LoRa™ Spread Spectrum Modulation technology with auto multi-level repeating.

<img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img.png" />

## For Communication between two Pi Lora Hat

<img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img4.JPG" />

* First take 2 LORA Hat board and set jumper position as mention below:
  * <b> Mode Selection Jumper :</b> we are going to use pi GPIO pin 13 and 15 to control MODE Selection
   * <b> LoRa mode selection jumpers 
     * <b> short M0, short M1: transmission mode (In this project we use transmission mode)
     * <b> short M0, open M1: configuration mode (You can configure the lora via this mode)
     * <b> open M0, short M1: WOR mode
     * <b> open M0, open M1: deep sleep mode
 
  * <b> Device Selection Jumper(Board Selection, This is also mention in the board) : 
    * </b> Set is as MODE 1 to enable USB to LORA Communication (Without raspberry pi)
    * </b> Set is as MODE 2 to enable PI to LORA Communication (With raspberry pi)

  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img2.png" />
 
 ## Code
 In this folder you see two python codes
   * Lora_transmitter.py -> run this file to transmit the data (any data eg: sensor data,any string and message etc)
   * Lora_receiver.py    -> run this file to receive data from other lora
     
**NOTE:** There is difference in latest Raspberry Pi 5 terminal use as compared to previous Pi 4 and 3. To Use LoRa HAT with Raspberry Pi 5 you will have to change Serial access port as shown in below code

```
# For previous Raspberry Pi 4 & 3
lora = serial.Serial(port = '/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)

# replace ttyS0 with ttyAMA0 for RPi 5 
lora = serial.Serial(port = '/dev/ttyAMA0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)

```
 ## Applications
 In this folder you see two application
   * Pi Lora Broadcast (with LCD display), In this folder you see three files
       * PCLinuxOSFonts -> this folder contains various fonts
       * transmitter.py -> run this file to broadcast the data (any data eg: sensor data,any string and message etc)
       * receiver.py    -> run this file to receive broadcast data from other lora
       * ST7789.py      -> this is the lcd library file
 
   * Pi Lora Homeautomation (with LCD display), In this folder you see three files
       * pi_lora_transmitter_home_automation.py
       * pi_lora_receiver_home_automation.py 
       * ST7789.py
 
 ## Our Other LoRa Products

* GatePi 4Channel
* GatePi 8channel
* RangePi
* LoRA HAT for RPi*
* PICO LoRa Expansion

You will simply need to make one device to work as reciever and another one is as a transmitter. So that you can communicate to each other and this can be done with any of our LoRa products mentioned above. For working with our other products please follow the below link:

* GatePi 4Channel
https://github.com/sbcshop/GatePi-4CH
* GatePi 8channel
https://github.com/sbcshop/GatePi-8CH
* RangePi
https://github.com/sbcshop/RangePi
* LoRA HAT for RPi* (Itself)
* PICO LoRa Expansion
https://github.com/sbcshop/PICO-LORA-EXPANSION


### Note: Every time you choose the mode of transmit device the transmit code of that device should be run in it and reciever code will always same (or depending upon what you want to control or recieve).
 
 ## Lora GUI For Configuration (run with the help of GUI)
 For this, you need to use Lora onboard USB 
 <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_18.jpg" />
 
 Go to the Lora GUI folder, and run the LORA_GUI.py file. from this file, you can configure the Lora and you are able to transmit, receive the data  (eg: baud rate, channel etc)
 Follow the steps to configure the Lora module:-

 ### Step 1: Setup lora in configuration mode, for this you need to short M0 and open M1 as shown in figure. In case of PICO LoRa Expansion find the mode selection jumper in that board and remove M1 jumper for config mode.
 
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_16.jpg" />
 
### Step 2: Open lora GUI 
 <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_1.png" />

### Step 3: set the COM Port and Baudrate
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_2.png" />
 
### Step 4: For COM Port go to Device Manager, before this first you need to connect the Lora module via USB cable 
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_7.png" />
 
### Step 5: Write the right COM Port in the GUI,then press connect button
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_8.png" />
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_9.png" />

### Step 6: Press read button to see the device configuration which lora already have
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img__10.png" />
 
### Step 7: Write the values which you need to configure, for eg: i configure channel and baudrate, after that press write button
  
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_13.png" />
  
**-> For changing frequency using Software for 868MHz & 915MHz LoRa module:**
  
  Frequency = 850.125MHz + CH*1MHz
  
  0-83 total of 84 Channel available
  
  So, when 5 selected
  Frequency = 850.125MHz + 5*1MHz
  Frequency = 855.125MHz 
  

  **-> For Changing Frequency using Software for 433MHz LoRa Module:**
  Frequency = 410.125MHz + CH*1MHz
  
  0-83 total of 84 Channel available
  
  So, when 5 selected
  Frequency = 410.125MHz + 5*1MHz
  Frequency = 415.125MHz
### Step 8: Restart the GUI, set baudrate and port, then connect and press read button 
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_14.png" />
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_15.png" />
 
 

### <a href="https://learn.sb-components.co.uk/LoRa-HAT-for-Raspberry-Pi" > LoRa HAT Wiki Portal </a>
 

