import requests
import PublicIP

ip = PublicIP.ip
port = '4900'

def run(command):
    url = 'http://'+ip+':'+port+'/' + command + '/'
    post = requests.post(url)

def On():
    run('0xFF02FD')


def Off():
    run('0xFF02FD')


def White():
    run('0xFF22DD')
