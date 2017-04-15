import requests

# url = 'https://antihta.herokuapp.com/getResponse/'
# params = {"hub.verify_token":"AntiHomeTheft","hub.challenge":"42"}
url="http://127.0.0.1:8000/getResponse/"
files = {'media': open('akash.jpg', 'rb')}
r = requests.post(url, data = {'id':'2507'},files=files)
import pdb; pdb.set_trace()