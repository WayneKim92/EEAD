from gpiozero import AngularServo
from time import sleep

# 0~90도 움직임
# servo = AngularServo(18, min_angle = 0, max_angle = 360)
# while True:
#     servo.angle = 0
#     sleep(3)
#     servo.angle = 180
#     sleep(3)
#     servo.angle = 359
#     sleep(3)

# 0 ~110도 움직임
# servo = AngularServo(18, min_angle = 0, max_angle = 180)
# while True:
#     servo.angle = 0
#     sleep(3)
#     servo.angle = 180
#     sleep(3)

# 그나마 정확한 수치
servo = AngularServo(18, min_angle = 0, max_angle = 120)
while True:
    servo.angle = 0
    sleep(3)
    servo.angle = 100
    sleep(3)

