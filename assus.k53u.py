from functools import partial
import RPi.GPIO as GPIO
import time, sys

# [GPIO] =========================================================
#
POWER_PIN  = 7 
STATUS_PIN = 22

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

GPIO.setup(POWER_PIN, GPIO.OUT) 
GPIO.setup(STATUS_PIN, GPIO.IN)

# [FUNCTION] =====================================================
#
def powerOn(status):
    if status != 1:
        GPIO.output(POWER_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(POWER_PIN, GPIO.LOW)
        out = showStatus(1, '>>> send.cmd->')
    else:
        out = showStatus(status, 'is:')
    return out
        
def powerOff(status):
    if status == 1:
        GPIO.output(POWER_PIN, GPIO.HIGH)
        time.sleep(4.5)
        GPIO.output(POWER_PIN, GPIO.LOW)        
        out = showStatus(0, '>>> send.cmd->')
    else:
        out = showStatus(status, 'is:')
    return out

def getStatus():
    if GPIO.input(STATUS_PIN) == 1:
        return 0
    else:
        return 1

def showStatus(status, message = ''):
    if status == 1:
        return message + "power:on"
    else:
        return message + "power:off"

def init(arg):
    status = getStatus()
    switcher = {
        'pw' : partial(powerOn, status),
        'pw4': partial(powerOff, status),
        'st' : partial(showStatus, status),
    }

    func = switcher.get(arg, lambda: "Available commands are: ['pw', 'pw4', 'st']")
    return func()

# [BEGIN] ========================================================
#
try:
    print("== [GPIO.INFO] ===================================")
    print("-=\t",GPIO.RPI_INFO['TYPE'],GPIO.RPI_INFO['RAM'],"GPIO.VER:",GPIO.VERSION,"\t=-")
    print("==================================================")
    
    if len(sys.argv) == 2:
        cmd = sys.argv[1]
    else:
        cmd = "undefined"
    
    output = init(cmd)
    print(output)
    
    GPIO.cleanup()
    print("==================================================")
except:
    GPIO.cleanup()