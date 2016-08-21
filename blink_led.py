import RPi.GPIO as GPIO
import time
import random

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)



for i in range (0,20):

    x = random.randint(11,15)
    y = random.randint(11,15)
    if( x != y  and x !=14 and y != 14):
        GPIO.output(x,True)
        GPIO.output(y,True)
        time.sleep(1)
        GPIO.output(x,False)
        GPIO.output(y,False)
        time.sleep(1)

GPIO.cleanup()


