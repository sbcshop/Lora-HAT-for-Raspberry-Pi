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
 
 ## Lora GUI For Configuration (run with the help of GUI)
 For this, you need to use Lora onboard USB 
 <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_18.jpg" />
 
 Go to the Lora GUI folder, and run the LORA_GUI.py file. from this file, you can configure the Lora and you are able to transmit, receive the data  (eg: baud rate, channel etc)
 Follow the steps to configure the Lora module:-

 ### Step 1: Setup lora in configuration mode, for this you need to short M0 and open M1 as shown in figure
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_16.jpg" />
 
### Step 2: Open lora GUI 
 <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_1.png" />

### Step 2: set the COM Port and Baudrate
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_2.png" />
 
### Step 3: For COM Port go to Device Manager, before this first you need to connect the Lora module via USB cable 
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_7.png" />
 
### Step 3: Write the right COM Port in the GUI,then press connect button
  <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_8.png" />
   <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/img_9.png" />
 
 <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/gui.JPG" />

### <a href="https://learn.sb-components.co.uk/LoRa-HAT-for-Raspberry-Pi" > LoRa HAT Wiki Portal </a>
 

