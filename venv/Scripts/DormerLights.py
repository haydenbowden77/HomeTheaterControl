import requests


def On():
    # print(bytes)
    post = requests.post('http://173.202.23.174:4900/0xFF02FD/')
    #print(post.response)


def Off():
    post = requests.post('http://173.202.23.174:4900/0xFF02FD/')
    #print(post.response)


def White():
    post = requests.post('http://173.202.23.174:4900/0xFF22DD/')
    #print(post.response)
