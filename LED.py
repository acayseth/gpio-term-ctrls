import RPi.GPIO as GPIO
import time


s=14


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(s, GPIO.OUT)

print "LED on"

GPIO.output(s, GPIO.HIGH)

time.sleep(4)

print "LED off"

GPIO.output(s, GPIO.LOW)


GPIO.cleanup()