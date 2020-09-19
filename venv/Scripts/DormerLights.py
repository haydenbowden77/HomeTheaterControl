import requests
import PublicIP

ip = PublicIP.ip
port = 4900

def On():
    # print(bytes)
    url = 'http://'+ip+':'+port+'/0xFF02FD/'
    post = requests.post(url)
    #print(post.response)


def Off():
    url = 'http://'+ip+':'+port+'/0xFF02FD/'
    post = requests.post(url)
    #print(post.response)


def White():
    url = 'http://'+ip+':'+port+'/0xFF22DD/'
    post = requests.post(url)
    #print(post.response)
