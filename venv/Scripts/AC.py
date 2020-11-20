import requests
import PublicIP

ip = PublicIP.ip
port = '4903'

def run(command):
    url = 'http://'+ip+':'+port+'/' + command + '/'
    post = requests.post(url)

def On():
    run('0x8166817E')

def Off():
    run('0x8166817E')

def ChangeMode():
    run('0x8166D926')

def TempUp():
    run('0x8166A15E')

def TempUp(amt):
    for i in range(amt):
        run('0x8166A15E')

def TempDown():
    run('0x816651AE')

def TempDown(amt):
    for i in range(amt):
        run('0x816651AE')