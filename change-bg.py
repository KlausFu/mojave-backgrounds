from datetime import datetime, timedelta
import subprocess
from subprocess import PIPE

time_now = datetime.now()
time_then = datetime.now().replace(hour=0, minute=30)
hasfound = 0
for _ in range(16):
    if time_now <= time_then:
        hasfound = 1
        break
    elif datetime.now().replace(hour=23, minute=00) < time_then < datetime.now().replace(hour=00, minute=30):
        hasfound = 1
        break
    else:
        time_then = time_then + timedelta(hours=1, minutes=30)

time_then = time_then - timedelta(hours=1, minutes=30)

if hasfound == 0:
    print "err"
else:
    hours = str(time_then.hour).zfill(2)
    minutes = str(time_then.minute).zfill(2)
    print hours + ":" + minutes
    subprocess.call(['osascript', '-e',
                     'tell application "System Events" to tell every desktop to set picture to "wallpapers/mojave-' + hours + '-' + minutes + '.jpeg"'],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE)
