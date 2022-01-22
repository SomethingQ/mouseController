import time
from helpers import setSpeed, checkKey, move, capsLock, blockkeys, unblockKeys

speed = 25
speedReduction = 5

pollingRate = 0.015  # ~60hz

keys = ['i', 'k', 'j', 'l', 's', 'd', 'w', 'f', 'v', 'shift']

setSpeed(speed, keys)

while True:
    if capsLock():
        blockkeys()
        checkKey(speedReduction)
        move()
    else:
        unblockKeys()

    time.sleep(pollingRate)
