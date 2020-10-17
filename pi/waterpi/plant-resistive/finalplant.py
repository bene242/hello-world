from gpiozero import DigitalInputDevice
import RPi.GPIO as GPIO
from time import sleep
import logging

logger = logging.getLogger('finalplant')
hdlr = logging.FileHandler('/home/pi/watering.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)
 
d0_input = DigitalInputDevice(17)

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
RELAIS_1_GPIO = 23
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus

if (not d0_input.value):
        print('Moisture threshold reached!!!')
        print(d0_input.value)
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
        logger.info('No watering needed')
        sleep(2)
else:
        print('You need to water your plant')
        print(d0_input.value)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
        sleep(2)
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
        logger.info('Plant is watered')


