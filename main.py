from gpiozero import MotionSensor
from picamera import PiCamera
# import os,sys
# from PIL import Image
import requests

camera = PiCamera()
pir = MotionSensor(4)
import time
count=0

def sendRequest(image):
	url = 'https://antihta.herokuapp.com/getResponse/'
	params = {"hub.verify_token":"AntiHomeTheft","hub.challenge":"42"}
	# url="http://127.0.0.1:8000/getResponse/"
	files = {'media': open(image, 'rb')}
	r = requests.post(url, data = {'key':'value'},files=files)
	print "image sent to fb"


while True:
	if pir.motion_detected:
		print "motion detected"
		count+=1
		name="/home/pi/Desktop/image"+str(count)+".jpg"
		camera.capture(name)
		# jpgfile = Image.open(name)
		# print jpgfile
		sendRequest(name)
		time.sleep(3)
	else:
		print "no motion"
