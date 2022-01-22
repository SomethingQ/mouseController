import keyboard
import mouse
import time

keys = []

x = 0
y = 0


def capsLock():
    import ctypes
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def setSpeed(speed, keyInput):
    global speedo, keys
    keys = keyInput
    speedo = speed


def blockkeys():
    global blocked
    if blocked:
        return

    for key in keys:
        keyboard.block_key(key)
    blocked = True


def unblockKeys():
    global blocked
    if blocked == False:
        return

    for key in keys:
        keyboard.unblock_key(key)
    blocked = False


blocked = False
on = True
ce = True
fb = True
a = 60
shift = True
acceleration = a

speedo = 0


def checkKey(speedReduction=5):
    global x, y, on, ce, fb, shift, acceleration, speedo

    if keyboard.is_pressed(keys[9]) and shift:
        speedo /= speedReduction
        acceleration = 0
        shift = False

    elif keyboard.is_pressed(keys[9]) == False and shift == False:
        speedo *= speedReduction
        acceleration = a
        shift = True

    if keyboard.is_pressed(keys[0]):
        y = -speedo
    elif keyboard.is_pressed(keys[1]):
        y = speedo
    else:
        y = 0
    if keyboard.is_pressed(keys[2]):
        x = -speedo
    elif keyboard.is_pressed(keys[3]):
        x = speedo
    else:
        x = 0

    if keyboard.is_pressed(keys[4]) and on:
        mouse.press('left')
        on = False
    elif keyboard.is_pressed(keys[4]) == False and on == False:
        on = True
        mouse.release('left')

    if keyboard.is_pressed(keys[5]) and ce:
        mouse.press('right')
        ce = False
    elif keyboard.is_pressed(keys[5]) == False and ce == False:
        ce = True
        mouse.release('right')

    if keyboard.is_pressed(keys[6]) and fb:
        mouse.press('middle')
        fb = False
    elif keyboard.is_pressed(keys[6]) == False and fb == False:
        fb = True
        mouse.release('middle')

    if keyboard.is_pressed(keys[7]):
        mouse.wheel(1)
        if shift:
            time.sleep(0.0005)
        else:
            time.sleep(0.08)
    elif keyboard.is_pressed(keys[8]):
        mouse.wheel(-1)
        if shift:
            time.sleep(0.0005)
        else:
            time.sleep(0.08)


def move():
    mouse.move(x, y, absolute=False, duration=0)
