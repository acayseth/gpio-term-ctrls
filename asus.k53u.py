import RPi.GPIO as GPIO
import time
import sys

# [SETUP GPIO PINS] ==============================================
#
POWER_PIN  = 25
STATUS_PIN = 7

# [GPIO] =========================================================
#
GPIO.setwarnings(True)
# GPIO.cleanup()       # ???
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(POWER_PIN, GPIO.OUT) 
GPIO.output(POWER_PIN, GPIO.HIGH)

GPIO.setup(STATUS_PIN, GPIO.IN)

# [Application] ==================================================
print("== [GPIO.INFO] ===================================")
print("-=\t",GPIO.RPI_INFO['TYPE'],GPIO.RPI_INFO['RAM'],"GPIO.VER:",GPIO.VERSION,"\t=-")
print("==================================================")

commands = ['pw', 'pw4', 'st']

if len(sys.argv) == 2:
    command = sys.argv[1]
else:
    command = "undefined"
    
def getStatus():
    if GPIO.input(STATUS_PIN) == 1:
        return 0
    else:
        return 1

def getStatusMessage(status):
    if status:
        print("power:on")
    else:
        print("power:off")
    

def powerOn(status):
    if status != 1:
        print("GPIO.output(POWER_PIN, GPIO.LOW)")
        # GPIO.output(POWER_PIN, GPIO.LOW)
        time.sleep(0.5)
        print("GPIO.output(POWER_PIN, GPIO.HIGH)")
        # GPIO.output(POWER_PIN, GPIO.HIGH)
        
        getStatusMessage(getStatus())
    else:
        print("power is on")

def powerOff(status):
    if status != 0:
        print("GPIO.output(POWER_PIN, GPIO.LOW)")
        # GPIO.output(POWER_PIN, GPIO.LOW)
        time.sleep(4.5)
        print("GPIO.output(POWER_PIN, GPIO.HIGH)")
        # GPIO.output(POWER_PIN, GPIO.HIGH)
        
        getStatusMessage(getStatus())
    else:
        print("Upsss... power is off")

if command == "pw":
    powerOn(getStatus())
elif command == "pw4":
    powerOff(getStatus())
elif command == "st":
     getStatusMessage(getStatus())
else:
    print("Available commands are:", commands)

print("==================================================")
GPIO.cleanup()