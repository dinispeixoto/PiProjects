import RPi.GPIO as GPIO
import time
from sys import argv
from led_controller import setupLed, ledON, ledOFF

sensor_gpio = int(argv[1])
led_gpio = int(argv[2])

def setupSoundSensor(n_gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n_gpio, GPIO.IN)

def callback(sensor_gpio):
    if GPIO.input(sensor_gpio):
        print "Sound detected"
        ledON(led_gpio)
        ledOFF(led_gpio)
    else:
        print "Sound detected"
        ledON(led_gpio)
        ledOFF(led_gpio)

def setup():
    setupLed(led_gpio)
    setupSoundSensor(sensor_gpio)
    GPIO.add_event_detect(sensor_gpio, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(sensor_gpio, callback)

def run():
    while True:
        time.sleep(1)

if __name__ == '__main__':
    setup()
    run()
