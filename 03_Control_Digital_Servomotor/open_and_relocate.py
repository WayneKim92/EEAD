from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle = -60, max_angle = 60)

servo.angle = -60
sleep(2)
servo.angle = 60
sleep(2)
