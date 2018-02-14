import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def setupButton(n_gpio):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(n_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonIsClicked(n_gpio):
    return GPIO.input(n_gpio)
