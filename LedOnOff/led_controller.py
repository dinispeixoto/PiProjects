import RPi.GPIO as GPIO
from sys import argv

GPIO.setwarnings(False)

def setupLed(n_gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n_gpio, GPIO.OUT)

def ON(n_gpio):
    GPIO.output(n_gpio, GPIO.HIGH)

def OFF(n_gpio):
    GPIO.output(n_gpio, GPIO.LOW)
