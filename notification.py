from win32gui import GetWindowText, GetForegroundWindow
from pushbullet import Pushbullet
import time 

pb = Pushbullet('API KEY HERE')
while GetWindowText(GetForegroundWindow()) != "Dota 2":
    time.sleep(1)
pb.push_note("GAME FOUND", "LETS GET IT")

e