import RPi.GPIO as GPIO
import logging
import sys
from time import sleep
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw


format_string = "%(asctime)s [%(levelname)s] - %(filename)s : %(message)s"
logger = logging.getLogger()
formatter = logging.Formatter(format_string)

file_handler = logging.FileHandler(filename="watering.log", mode="a")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)
touch = ss.moisture_read()
temp = ss.get_temp()
temp = round(temp,2)
logging.debug("temp: " + str(temp) + " moisture: " + str(touch))


GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 23
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

print("relais to HIGH")
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
sleep(2)
print("relais to LOW")
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
sleep(2)
print("relais to HIGH")
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus

logging.debug("Watering done")
