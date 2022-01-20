from lora_hat import LoraHat

#  Initialize Lora class
lora = LoraHat()

#  Initialize serial port with com port and baud rate
lora.connect_hat(port="COM17", baud_rate=9600)

#  Set LORA Module to configuration mode
lora.configuration_mode()

#  Set variables, check datasheet for variable details
lora._baud_rate = 0b011
lora._parity = 0b00
lora._air_data_rate = 0b010

lora._packet_size = 0b00
lora._packet_rssi = 0b0
lora._transmit_power = 0b00

lora._channel_rssi = 0b0
lora._transmission_mode = 0b0
lora._reply = 0b0
lora._lbt = 0b0
lora._wor_tx_control = 0b0
lora._wor_cycle = 0b011

lora._module_address = 0x0000
lora._net_id = 0x00
lora._channel = 0x32
lora._encrypt_key = 0

#  Write data to LORA Module
lora.write_all_configuration()

#  Wait for Rx Data from LORA Hat
while not lora.rxData:
    pass

#  Print Received data
print(lora.rxData)

#  Disconnect Lora hat
lora.disconnect_hat()
