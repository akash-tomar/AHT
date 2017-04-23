from gpiozero import MotionSensor
from picamera import PiCamera
# import os,sys
# from PIL import Image
import requests
import json
camera = PiCamera()
pir = MotionSensor(4)
import time
count=0

def sendRequest(image):
	url = 'https://antihta.herokuapp.com/getResponse/'
	params = {"hub.verify_token":"AntiHomeTheft","hub.challenge":"42"}
	# url="http://127.0.0.1:8000/getResponse/"
	files = {'media': open(image, 'rb')}
	r = requests.post(url, data = {'id':'2507'},files=files)
	print "image sent to fb"


def shutDown():
    command = "sudo poweroff"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

def getRequest():
	url = 'https://antihta.herokuapp.com/kill/?id=2507'
	params = {"hub.verify_token":"AntiHomeTheft","hub.challenge":"42"}
	# url = 'http://127.0.0.1:8000/kill/?id=2507'
	# url="http://127.0.0.1:8000/getResponse/"
	# files = {'media': open(image, 'rb')}
	r = requests.get(url)
	print "pi shut down request"
	kill = json.loads(r._content)
	if kill:
		#shut down pi
		shutDown()


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
