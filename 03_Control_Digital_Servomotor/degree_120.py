from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle=0, max_angle=120, min_pulse_width=0.0005, max_pulse_width=0.0025)

servo.angle = 100