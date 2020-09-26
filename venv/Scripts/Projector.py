from pypjlink import Projector
import requests
import socket


def powerOn():
    '''message = 'POST /tgi/control.tgi HTTP/1.1\r\n'  \
            'Host: 192.168.1.146\r\n'   \
            'Connection: keep-alive\r\n'    \
            'Content-Length: 18\r\n'    \
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36\r\n'   \
            'Content-type: application/x-www-form-urlencoded\r\n'   \
            'Accept: */*\r\n'   \
            'Origin: http://192.168.1.146\r\n'  \
            'Referer: http://192.168.1.146/control.htm\r\n' \
            'Accept-Encoding: gzip, deflate\r\n'    \
            'Accept-Language: en-US,en;q=0.9\r\n'   \
            'Cookie: ATOP=NmDId\r\n'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.146',80))
    sock.send(message.encode())'''




               # 'POST /tgi/control.tgi HTTP/1.1\r\n' \
              #'Content-Type: application/x-www-form-urlencoded\r\n' \
              #'Content-Length: 18\r\n' \
              #'Host: http://192.168.1.146\r\n'

    cookies = dict(ATOP='NmDId')
    headers = {
        'Referer': 'http://192.168.1.146/control.htm',
        'Origin': 'http://192.168.1.146',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    data = {'btn_powon':'Power On','pw': "0"}
    r = requests.post('http://192.168.1.146:80/tgi.control.tgi', data=data, headers=headers)
    #with Projector.from_address('192.168.1.146') as optoma:
     #   optoma.authenticate('admin')
      #  optoma.set_power('on')

def powerOff():

    r = requests.post('192.168.1.146', data={'btn_powoff':'Power Off'})
    #with Projector.from_address('192.168.1.146') as optoma:
     #   optoma.authenticate('admin')
      #  optoma.set_power('standby')
