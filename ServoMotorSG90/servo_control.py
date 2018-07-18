import RPi.GPIO as GPIO
import time

servo_gpio = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_gpio, GPIO.OUT)

p = GPIO.PWM(servo_gpio, 50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop(
    GPIO.cleanup()
