from lora_hat import LoraHat

#  Initialize Lora class
lora = LoraHat()

#  Initialize serial port with com port and baud rate
lora.connect_hat(port="COM17", baud_rate=9600)

#  Set LORA module to Normal mode
lora.normal_mode()

#  Transmit message
message = "Hello, This is LORA Test"
lora.transmit_message(bytes(message, "utf-8"))

#  Wait for Rx Data from LORA Hat
while not lora.rxData:
    pass

#  Print Received Message
print(lora.rxData)

#  Disconnect Lora hat
lora.disconnect_hat()
