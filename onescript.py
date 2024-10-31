import importlib.util
import os
import time
import datetime

file = __file__ + ':'


# The magic
def read_internal_file(f, w):
    with open(file + f, w) as f:
        return f.read()


def load_internal_module(f):
    spec = importlib.util.spec_from_file_location('', os.path.realpath(file + f))
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


print(read_internal_file('welcomeText', 'r'))  # Welcome text

# Load modules
terminal = load_internal_module('terminal.py')
pe = load_internal_module('pygameextra_import.py')
tsx = pe.tsx
math = pe.math
g = load_internal_module('graphics.py')

input("Press enter to continue -> ")
g.clear()
terminal.font((1, 1))
g.resize((400, 400))

# SCREEN SIZE

S = 200
g.resize((S, S))
terminal.font((1, 1))
g.clear()

# CLOCK

g.setColor(g.blue)
middle = (S / 2, S / 2)
tsxS = tsx.TSX((S / 2, S / 2), (S / 2) - (S / 19), -90)
tsxM = tsx.TSX((S / 2, S / 2), (S / 2) - (S / 6), -90)
tsxH = tsx.TSX((S / 2, S / 2), (S / 2) - (S / 3.5), -90)
mainTSX = tsx.TSX((S / 2, S / 2), (S / 2) - (S / 20), -90)
secondANGLE = 180
minuteANGLE = 90
hourANGLE = 45


def secondLine(x, y, c):
    g.circle(x, y, int(S / 150), S, S, c)


def minuteLine(x, y, c):
    g.circle(x, y, int(S / 100), S, S, c)


def hourLine(x, y, c):
    g.circle(x, y, int(S / 80), S, S, c)


passed = 0
sAC = 360 / 60
msAC = sAC / 1000000
mAC = 360 / 60
hAC = 360 / 12
t = datetime.datetime.now()
lastsecondANGLE = secondANGLE
lastminuteANGLE = minuteANGLE
begin = True
lasthourANGLE = hourANGLE
secondANGLE = (t.second * sAC) + (t.microsecond * msAC)
minuteANGLE = t.minute * mAC
hourANGLE = t.hour * hAC
prev = 0

while True:
    t = datetime.datetime.now()
    lastsecondANGLE = secondANGLE
    lastminuteANGLE = minuteANGLE
    lasthourANGLE = hourANGLE
    secondANGLE = (t.second * sAC) + (t.microsecond * msAC)
    minuteANGLE = t.minute * mAC
    hourANGLE = t.hour * hAC
    if lastsecondANGLE != secondANGLE:
        for i in range(prev, int(secondANGLE)):
            l = tsxS[i]
            g.circle(*g.cap(l[0], l[1], S, S), int(S / 90), S, S, g.purple)
        prev = int(secondANGLE)
    if int(lastminuteANGLE) != int(minuteANGLE) or begin:
        begin = False
        g.line(*g.cap(*middle, S, S), *g.cap(*tsxM[int(lastminuteANGLE)], S, S), S, S, g.black,
               minuteLine)
        g.line(*g.cap(*middle, S, S), *g.cap(*tsxH[int(hourANGLE)], S, S), S, S, g.black, hourLine)

        g.line(*g.cap(*middle, S, S), *g.cap(*tsxM[int(minuteANGLE)], S, S), S, S, g.red, minuteLine)
        g.line(*g.cap(*middle, S, S), *g.cap(*tsxH[int(hourANGLE)], S, S), S, S, g.green, hourLine)
        for i in range(360):
            l = tsxS[i]
            g.circle(*g.cap(l[0], l[1], S, S), int(S / 90), S, S, g.black)
            l = mainTSX[i]
            g.circle(*g.cap(l[0], l[1], S, S), int(S / 110), S, S)
        prev = 0

input()
g.clear()

input()
