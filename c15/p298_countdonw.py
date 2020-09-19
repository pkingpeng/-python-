#! python3
# A simple countdown script.
# 十秒计时然后播放音乐

import time, subprocess

timeLeft = 10

while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['open', '../resource/audio/alarm.wav'])
