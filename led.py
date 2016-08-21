import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)


try : 
    while True:
        GPIO.output(11,GPIO.HIGH)

        time.sleep(0,15)

        GPIO.output(11,GPIO.LOW)
except KeyboardInterrupt:
    print("\nkeyboard has been detected!")

except:
    print("\An error or exception has occured!")

finally:
    GPIO.cleanup()
