import time
from helpers import setSpeed, checkKey, move, capsLock, blockkeys, unblockKeys, enableProgram

speed = 25
speedReduction = 5

pollingRate = 0.015  # ~60hz

enableKey = 'q'
keys = ['i', 'k', 'j', 'l', 's', 'd', 'w', 'f', 'v', 'shift', enableKey]

setSpeed(speed, keys)

while True:
    if capsLock():
        blockkeys()
        checkKey(speedReduction)
        move()
    else:
        unblockKeys()

    time.sleep(pollingRate)
