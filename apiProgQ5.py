import requests
import traceback
import json

def postMethod():
    
    url = 'https://dev.rackspace.example.com/widgets'
    header={"content-type":"application/json","Authorization":"5675309"}
    payload = {"widget_name": "Test Widget","description": "Description"}
    
    r = requests.post(url, data=payload)
    print r.text
    print r.status_code
    
    
if __name__=="__main__":
    postMethod()
