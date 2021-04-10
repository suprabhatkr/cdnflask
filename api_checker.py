import requests
import json
url = "http://127.0.0.1:5000/"

#r= requests.get(url= url) 
data = {'url':'http://example.com','content':'hello bro\n'}
data = json.dumps(data) 
r= requests.post(url=url,data=data)
print(r.text) 
r= requests.get(url=url)
print(r.text)
