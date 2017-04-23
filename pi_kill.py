import requests

def sendRequest():
	url = 'https://antihta.herokuapp.com/kill/?id=2507'
	params = {"hub.verify_token":"AntiHomeTheft","hub.challenge":"42"}
	# url = 'http://127.0.0.1:8000/kill/?id=2507'
	# url="http://127.0.0.1:8000/getResponse/"
	# files = {'media': open(image, 'rb')}
	r = requests.get(url)
	import pdb; pdb.set_trace()
	print "image sent to fb"
sendRequest()
