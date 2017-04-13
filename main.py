from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
import time
count=0
while True:
    if pir.motion_detected:
	print "motion detected"
	count+=1
	name="/home/pi/Desktop/image"+str(count)+".jpg"
    	camera.capture(name)
	time.sleep(1)
    else:
	print "no motion"
