import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 23
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
sleep(2)
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # an
		
sleep(2)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aus
