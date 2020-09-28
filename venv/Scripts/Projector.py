from pypjlink import Projector
import requests
import socket
import urllib.request

def getChallenge(html):
    html = str(html)
    index = html.find('Challenge')
    html = html[index:len(html):]
    index = html.find('VALUE')
    html = html[index:len(html):]
    index = html.find('"')
    html = html[index+1:len(html):]
    index = html.find('"')
    html = html[0:index:]
    return html

def powerOn():
    session = requests.Session()
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    data = {'user':'0',
            'Username':'1',
            'Password':'',
            'Challenge':'',
            'Response':'2c3b09ef8ad3e94bd60ab8c6ea2e07d5'}
    cookies = {'ATOP': 'PSa.d'}
    s = requests.get('http://192.168.1.146:80/login.htm')
    challenge = getChallenge(s.content)
    str = 'adminadmin' + challenge
    print(challenge)
    #session.post('http://192.168.1.146:80/tgi/login.tgi',headers=headers,data = data,cookies=cookies)
    #,cookies=cookies)
    print(session.cookies.get_dict())
    '''url = 'http://192.168.1.146:80/tgi/control.tgi'
    data = {'btn_powon':'Power On'}
    #data = 'btn_powoff=Power Off'
    cookies = {'ATOP':'PSa.d'}
    session.post(url, headers=headers, data=data,cookies=cookies)'''


    '''
    with Projector.from_address('192.168.1.146') as optoma:
        optoma.authenticate('admin')
        optoma.set_power('on')'''

def powerOff():

    r = requests.post('192.168.1.146', data={'btn_powoff':'Power Off'})
    #with Projector.from_address('192.168.1.146') as optoma:
     #   optoma.authenticate('admin')
      #  optoma.set_power('standby')
