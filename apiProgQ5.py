"""As the given api didnt work, I have performed this using a restful localhost"""
import requests
import traceback
import json

def postMethod(url):

    try:
        
        header={"content-type":"application/json"}
        payload = {"widget_name": "Test Widget","description": "Description"}
        
        r = requests.post(url, data=json.dumps(payload), headers=header)
        print r.text
        print r.status_code
    except Exception,e:
        print e
        
def getMethod(url):
    try:
        val=requests.get(url)
        
        data = r.json() 
        print data
    except Exception,e:
        print e
        
def putMethod(url):

    try:
        
        header={"content-type":"application/json"}
        payload = {"widget_name": "Test Widget New"}
        
        r = requests.put(url, data=json.dumps(payload), headers=header)
        print r.text
        print r.status_code
    except Exception,e:
        print e
        
def deleteMethod(url):
    try:
        payload = {'widget_name':'Test Widget New'}
        headers = {'content-type': 'application/json'}
        
        r = requests.delete(url, data=json.dumps(payload), headers=header)        
        print r.text
        print r.status_code
    except Exception,e:
        print e
    
if __name__=="__main__":
    testUrl='https://localhost/widgets.php'
    """Choose your operation by commenting out rest"""
    postMethod(testUrl)
    getMethod(testUrl)
    putMethod(testUrl)
    deleteMethod(testUrl)
