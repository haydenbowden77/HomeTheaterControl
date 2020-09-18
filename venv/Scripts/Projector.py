from pypjlink import Projector

def powerOn():
    with Projector.from_address('192.168.1.146') as optoma:
        optoma.authenticate('admin')
        optoma.set_power('on')

def powerOff():
    with Projector.from_address('192.168.1.146') as optoma:
        optoma.authenticate('admin')
        optoma.set_power('standby')

