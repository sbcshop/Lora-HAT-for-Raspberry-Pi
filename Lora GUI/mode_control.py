from time import sleep
import logging
import os

os_name = os.name
if os_name == "posix":
    import RPi.GPIO as GPIO

"""
M0  M1  Mode
0   0   Normal/Transmission Mode
0   1   WOR Mode
1   0   Configuration Mode
1   1   Deep Sleep Mode
"""


class ModeControl(object):
    __M0 = 13  # Pin 22
    __M1 = 15  # Pin 17
    log = logging.getLogger("LORA ")
    log.addHandler(logging.StreamHandler())
    logging.basicConfig(filename='.log.log', level=logging.DEBUG)

    def __init__(self):
        self.__mode_set_time = .2
        self.gpio_setup()

    def __del__(self):
        if os_name == "posix":
            GPIO.cleanup()

    def gpio_setup(self):
        if os_name == "posix":
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(self.__M0, GPIO.OUT)
            GPIO.setup(self.__M1, GPIO.OUT)

            GPIO.output(self.__M0, GPIO.LOW)
            GPIO.output(self.__M1, GPIO.HIGH)
            sleep(self.__mode_set_time)
            self.log.info("GPIO initialized for M0 and M1.")

    def normal_mode(self):
        if os_name == "posix":
            GPIO.output(self.__M0, GPIO.LOW)
            GPIO.output(self.__M1, GPIO.LOW)
            sleep(self.__mode_set_time)
            self.log.info("LORA module set to normal mode.")

    def wor_mode(self):
        if os_name == "posix":
            GPIO.output(self.__M0, GPIO.LOW)
            GPIO.output(self.__M1, GPIO.HIGH)
            sleep(self.__mode_set_time)
            self.log.info("LORA module set to WOR mode.")

    def configuration_mode(self):
        if os_name == "posix":
            GPIO.output(self.__M0, GPIO.HIGH)
            GPIO.output(self.__M1, GPIO.LOW)
            sleep(self.__mode_set_time)
            self.log.info("LORA module set to Configuration mode.")

    def deep_sleep_mode(self):
        if os_name == "posix":
            GPIO.output(self.__M0, GPIO.HIGH)
            GPIO.output(self.__M1, GPIO.HIGH)
            sleep(self.__mode_set_time)
            self.log.info("LORA module set to Deep Sleep Mode mode.")

