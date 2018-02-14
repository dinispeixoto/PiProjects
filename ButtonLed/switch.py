import RPi.GPIO as GPIO
import time
from sys import argv
from led_controller import setupLed, ledON, ledOFF
from button_controller import setupButton, buttonIsClicked

button_gpio = int(argv[1])
led_gpio = int(argv[2])

def setup():
   setupButton(button_gpio)
   setupLed(led_gpio)

def run():
    while True:
        if buttonIsClicked(button_gpio) == False:
            ledON(led_gpio)
            time.sleep(1)
            ledOFF(led_gpio)

if __name__ == '__main__':
    setup()
    run()

