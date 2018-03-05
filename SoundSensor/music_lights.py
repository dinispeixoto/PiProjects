import RPi.GPIO as GPIO
import time
from sys import argv
from led_controller import setupLed, ledON, ledOFF

sensor_gpio = int(argv[1])
led_gpio = int(argv[2])

def setupSoundSensor(n_gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n_gpio, GPIO.IN)

def setup():
    setupLed(led_gpio)
    setupSoundSensor(sensor_gpio)

def run():
    while True:
        if GPIO.input(sensor_gpio) == GPIO.LOW:
            ledOFF(led_gpio)
        else:
            ledON(led_gpio)

if __name__ == '__main__':
    setup()
    run()
