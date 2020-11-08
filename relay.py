import RPi.GPIO as GPIO
import time, os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 

relay=4

GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, 0)
# os.system("clear")

try:
  print("Relay ON")

  GPIO.output(relay, 1)
  
  time.sleep(3)

  GPIO.output(relay, 0)

  print("Relay OFF")

  GPIO.cleanup()
except:
  print("exceprion")
  GPIO.cleanup()