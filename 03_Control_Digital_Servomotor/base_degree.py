from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle = 0, max_angle = 120)

servo.angle = 100
sleep(2)
