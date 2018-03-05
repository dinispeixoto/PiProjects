import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

def setupSoundSensor(n_gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n_gpio, GPIO.IN)


def callback(n_gpio):
    if GPIO.input(n_gpio):
        print "Sound detected"
    else:
        print "Sound detected"

n_gpio = 18
setupSoundSensor(n_gpio)
GPIO.add_event_detect(n_gpio, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(n_gpio, callback)

while True:
    time.sleep(1)
