from mode_control import ModeControl
from serial_comm import SerialComm
from time import sleep

# Configuration Commands
SET_REGISTER_COMMAND = 0xC0
READ_REGISTER_COMMAND = 0xC1
SET_TEMP_REGISTER_COMMAND = 0xC2
WIRELESS_CONF_COMMAND = 0xCFCF
WRONG_FORMAT_RESPONSE = 0xFFFFFF

# Register Address
MODULE_ADDRESS = 0x00
NET_ID_ADDRESS = 0x02
REG0_ADDRESS = 0x03  # UART(3), Parity(2), Air Data Rate(3)
REG1_ADDRESS = 0x04  # Sub Packet(2), RSSi(1), Reserve(3), Tx Power(2)
CHANNEL_CONTROL_ADDRESS = 0x05  # 0-80(81Channels), Freq = 850.125 + CH * 1M
REG3_ADDRESS = 0x06
CRYPT_ADDRESS = 0x07
PRODUCT_INFO_ADDRESS = 0x80  # 80-86


class LoraHat(ModeControl, SerialComm):
    def __init__(self):
        ModeControl.__init__(self)
        SerialComm.__init__(self)

        #  variables
        self._baud_rate = 0b011
        self._parity = 0b00
        self._air_data_rate = 0b010

        self._packet_size = 0b00
        self._packet_rssi = 0b0
        self._transmit_power = 0b00

        self._channel_rssi = 0b0
        self._transmission_mode = 0b0
        self._reply = 0b0
        self._lbt = 0b0
        self._wor_tx_control = 0b0
        self._wor_cycle = 0b011

        self._module_address = 0x0000
        self._net_id = 0x00
        self._channel = 0x32
        self._encrypt_key = 0

    def connect_hat(self, port, baud_rate):
        self.connect_port(port=port, baud_rate=baud_rate, timeout=0.5)

    def disconnect_hat(self):
        self.disconnect()

    def transmit_message(self, data):
        self.write(data)

    def write_all_configuration(self):
        data = self._config_tx_data()
        data_packet = [SET_REGISTER_COMMAND, MODULE_ADDRESS, len(data)] + data
        data_packet_array = bytearray(data_packet)
        self.configuration_mode()
        sleep(.04)
        self.write(data_packet_array)

    def read_configuration_data(self):
        data_packet = [READ_REGISTER_COMMAND, MODULE_ADDRESS, 9]
        data_packet_array = bytearray(data_packet)
        self.configuration_mode()
        sleep(.04)
        self.write(data_packet_array)

    def set_variables(self):
        pass

    def _config_tx_data(self):
        self.set_variables()
        data_array = [self._module_address >> 8, self._module_address & 0xFF,
                      self._net_id,
                      (self._baud_rate << 5) | (self._parity << 3) |
                      self._air_data_rate,
                      (self._packet_size << 6) | (self._packet_rssi << 5) |
                      0b000 | self._transmit_power,
                      self._channel,
                      (self._channel_rssi << 7) |
                      (self._transmission_mode << 6) | (self._reply << 5) |
                      (self._lbt << 4) |
                      (self._wor_tx_control << 3) | self._wor_cycle,
                      self._encrypt_key >> 8, self._encrypt_key & 0xFF
                      ]
        return data_array

    # Set Registers
    @staticmethod
    def _read_module_address(length):
        return [READ_REGISTER_COMMAND, MODULE_ADDRESS, length]

    @staticmethod
    def _write_module_address(parameter, write_type, length):
        write_add = 0x00
        if write_type:
            write_add = SET_REGISTER_COMMAND
        elif not write_type:
            write_add = SET_TEMP_REGISTER_COMMAND
        return [write_add, MODULE_ADDRESS, length, parameter]

