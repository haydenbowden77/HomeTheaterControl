import DirectPy

dtv = DirectPy.DIRECTV(ip='192.168.1.143',clientAddr='C42795D03F08')
#dtv = DirectPy.DIRECTV(ip='192.168.1.143',clientAddr='88F7C7A82F8B')

box.port = 4905
box.channel = '0'
box.valid_keys = ['power', 'poweron', 'poweroff', 'format', 'pause', 'rew', 'replay', 'stop', 'advance', 'ffwd', 'record',
                  'play', 'guide', 'active', 'list', 'exit', 'back', 'menu', 'info', 'up', 'down', 'left', 'right',
                  'select', 'red', 'green', 'yellow', 'blue', 'chanup', 'chandown', 'prev', '0', '1', '2', '3', '4', '5',
                  '6', '7', '8', '9', 'dash', 'enter']

def PowerOn()
#dtv.standby()

def TuneSEC
#dtv.tune_channel('611')

def Tune???
#dtv.tune_channel('233')

def Tune
#print(dtv.get_tuned())
"""def tune_channel(self, channel: "'###' or '###-#'"):
    """Change the channel on the receiver."""
    if not type(channel) is str:
        raise TypeError('Channel should be a string')
    major, minor = self._parse_channel(channel)

    jResp = requests.get(
        '%s/tv/tune?major=%s&minor=%s&clientAddr=%s' %
        (self.base_url, major, minor, self.clientAddr)).json()
    if jResp['status']['code'] == 200:
        self.channel = channel

    return jResp
"""
def Guide
#dtv.key_press("guide")

def Select
#dtv.key_press("select")

def List
#dtv.key_press("list")

def Play
#dtv.key_press("play")

def Pause
#dtv.key_press("pause")

def Stop
#dtv.key_press("stop")

def Rewind
#dtv.key_press("rew")

def FastForward
#dtv.key_press("ffwd")

def Replay
#dtv.key_press("replay")

def Advance
#dtv.key_press("advance")

def Record
#dtv.key_press("record")

def List
#dtv.key_press("list")

def Menu
#dtv.key_press("menu")

def Back
#dtv.key_press("back")

def Exit
#dtv.key_press("exit")

def Info
#dtv.key_press("info")

def Up
# dtv.key_press("up")

def Down
#dtv.key_press("down")

def Left
#dtv.key_press("left")

def Right
#dtv.key_press("right")

def Select
#dtv.key_press("select")

def ChanUp
#dtv.key_press("chanup")

def ChanDown
#dtv.key_press("chandown")

def Previous
#dtv.key_press("prev")

def Enter
#dtv.key_press("enter")