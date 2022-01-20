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
 
 ## Lora GUI (run with the help of GUI)
 For this you need to use lora onboard usb (use jumper wire at board selection 1)
 Go to Lora GUI folder, and run LORA_GUI.py file. from this file you can configure the Lora and you able to transmit,receive the data  (eg: baud rate,channel etc)
 
 <img src= "https://github.com/sbcshop/Lora-HAT-for-Raspberry-Pi/blob/main/images/gui.JPG" />
 

