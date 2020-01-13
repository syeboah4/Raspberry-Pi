import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

i = 0
while (i < 3):
    GPIO.output(17, GPIO.HIGH)
    print("Light On!")
    sleep(4) # Sleep for 4 second
    
    GPIO.output(17, GPIO.LOW) # Turn off
    print("Light Off!")
    sleep(2) # Sleep for 2 second
    i += 1

GPIO.cleanup()
