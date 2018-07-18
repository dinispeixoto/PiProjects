import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

servo_gpio = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_gpio, GPIO.OUT)

p = GPIO.PWM(servo_gpio, 50) # GPIO for PWM with 50Hz
p.start(2.5) # Init

try:
    while True:
        p.ChangeDutyCycle(5)
        time.sleep(0.1)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.1)
        p.ChangeDutyCycle(10)
        time.sleep(0.1)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.1)
        p.ChangeDutyCycle(10)
        time.sleep(0.1)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.1)
        p.ChangeDutyCycle(5)
        time.sleep(0.1)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
