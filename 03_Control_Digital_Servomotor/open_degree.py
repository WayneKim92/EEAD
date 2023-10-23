from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle = 0, max_angle = 120)

servo.angle = 0
sleep(2)
