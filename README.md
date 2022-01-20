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

