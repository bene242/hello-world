from gpiozero import DigitalInputDevice
from gpiozero import LED

import time
 
d0_input = DigitalInputDevice(17)

servo = LED(23)

while True:
    if (not d0_input.value):
        print('Moisture threshold reached!!!')
        servo.off()
        time.sleep(2)

    else:
        print('You need to water your plant')
        servo.on()
        time.sleep(2)
        servo.off()
