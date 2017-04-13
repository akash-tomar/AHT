from gpiozero import MotionSensor
import time
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("Motion detected!")
    else:
	print("no motion")
    time.sleep(0.1)
