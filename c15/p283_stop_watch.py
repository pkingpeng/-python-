#! python3
# A simple stopwatch program.

import time

print('Press Enter to begin. Afterwards, press Enter to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        now = time.time()
        lapTime = round(now - lastTime, 2)
        totalTime = round(now - startTime, 2)
        # print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime))
        # 优化显示
        print('Lap #' + str(lapNum).rjust(2) + ':'
              + str(totalTime).rjust(5) + ' (' + str(lapTime).rjust(5) + ')')
        lapNum += 1
        lastTime = now
except KeyboardInterrupt:
    print('\n Done.')
