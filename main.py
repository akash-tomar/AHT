from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
import time
while True:
    if pir.motion_detected:
    	camera.capture('/home/pi/Desktop/image.jpg')
	time.sleep(5)
