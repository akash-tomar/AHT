import requests
url = 'http://127.0.0.1:8000/getResponse/'
files = {'media': open('akash.jpg', 'rb')}
r = requests.post(url, data = {'key':'value'},files=files)
import pdb; pdb.set_trace()