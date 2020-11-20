import requests
import PublicIP
ip =  PublicIP.ip
port = '4902'
urlPrefix = 'http://' + ip + ':' + port + '/goform/formiPhoneAppDirect.xml?'

def run(command):
    postURL = 'http://' + ip + ':' + port + '/goform/AppCommand.xml'
    post = requests.post(postURL)
    url = urlPrefix + command
    r = requests.get(url)

#Power
def powerOn():
    run('PWON')

def powerOff():
    run('PWSTANDBY')

#Inputs
def playstation():
    run('SIGAME')

def computer():
    run('SIDVD')

def directv():
    run('SISAT/CBL')

def xbox():
    run('SIBD')

def bluetooth():
    run('SIBT')

#Outputs
def displayProjector():
    run('VSMONI1')

def displayComputer():
    run('VSMONI2')

def dualDisplay():
    run('VSMONIAUTO')

#Volume
def volumeUp():
    run('MVUP')

def volumeUp(amt):
    for i in range(amt):
        run('MVUP')

def volumeDown():
    run('MVDOWN')

def volumeDown(amt):
    for i in range(amt):
        run('MVDOWN')

def setVolume(vol):
    level = 'MV' + str(vol)
    run(level)

def mute():
    run('MUON')

def unmute():
    run('MUOFF')