import requests

def powerOn():
    post = requests.post('http://192.168.1.104:8080/goform/AppCommand.xml')
    r = requests.get('http://192.168.1.104:8080/goform/formiPhoneAppDirect.xml?PWON')

def powerOff():
    post = requests.post('http://192.168.1.104:8080/goform/AppCommand.xml')
    r = requests.get('http://192.168.1.104:8080/goform/formiPhoneAppDirect.xml?PWSTANDBY')

def playstation():
    post = requests.post('http://192.168.1.104:8080/goform/AppCommand.xml')
    r = requests.get('http://192.168.1.104:8080/goform/formiPhoneAppDirect.xml?SIGAME')

def projector():
    post = requests.post('http://192.168.1.104:8080/goform/AppCommand.xml')
    r = requests.get('http://192.168.1.104:8080/goform/formiPhoneAppDirect.xml?VSMONI1')

def computerScreen():
    post = requests.post('http://192.168.1.104:8080/goform/AppCommand.xml')
    r = requests.get('http://192.168.1.104:8080/goform/formiPhoneAppDirect.xml?VSMONI2')

def dualOutput():
    post = requests.post('http://192.168.1.104:8080/goform/AppCommand.xml')
    r = requests.get('http://192.168.1.104:8080/goform/formiPhoneAppDirect.xml?VSMONIAUTO')


