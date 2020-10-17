import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern
 
RELAIS_1_GPIO = 23
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Modus zuweisen

print("relais to HIGH")
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
sleep(1)
print("relais to LOW")
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # an
sleep(1)
print("relais to HIGH")
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aus
