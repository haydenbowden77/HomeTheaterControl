import requests


def On():
    post = requests.post('http://173.202.23.174:4900/0xFF02FD/')
    #print(post.status_code)


def Off():
    post = requests.post('http://173.202.23.174:4900/0xFF02FD/')
    #print(post.status_code)


def White():
    post = requests.post('http://173.202.23.174:4900/0xFF22DD/')
    #print(post.status_code)
