from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle = 0, max_angle = 90)

while True:
    for i in range(0,90,1):
        servo.angle = i
        sleep(0.1)
    for i in range(90,0,-1):
        servo.angle = i
        sleep(0.1)
