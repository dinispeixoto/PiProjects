import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def setupLed(n_gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n_gpio, GPIO.OUT)

def ledON(n_gpio):
    GPIO.output(n_gpio, GPIO.HIGH)

def ledOFF(n_gpio):
    GPIO.output(n_gpio, GPIO.LOW)
