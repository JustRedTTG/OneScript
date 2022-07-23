import importlib.util
import os
import time
import datetime

file = __file__+':'
# The magic
def read_internal_file(f,w):
    with open(file+f,w) as f:
        return f.read()
def load_internal_module(f):
    spec = importlib.util.spec_from_file_location('', os.path.realpath(file+f))
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo
print(read_internal_file('welcomeText', 'r')) # Welcome text

# Load modules
terminal = load_internal_module('terminal.py')
rom = load_internal_module('pgerom.py')
math = rom.math
g = load_internal_module('graphics.py')

input("Press enter to continue -> ")
g.clear()
terminal.font((1,1))
g.resize((400, 400))

# SCREEN SIZE

S = 200
g.resize((S, S))
terminal.font((1,1))
g.clear()

# CLOCK

g.setColor(g.blue)
middle = (S/2,S/2)
tsxS = math.tsx.make((S/2, S/2),(S/2)-(S/19))
tsxM = math.tsx.make((S/2, S/2),(S/2)-(S/6))
tsxH = math.tsx.make((S/2, S/2),(S/2)-(S/3.5))
tsx = math.tsx.make((S/2, S/2),(S/2)-(S/20))
secondANGLE = 180
minuteANGLE = 90
hourANGLE = 45
def secondLine(x,y,c):
    g.circle(x, y, int(S/150), S, S,c)
def minuteLine(x,y,c):
    g.circle(x, y, int(S/100), S, S,c)
def hourLine(x,y,c):
    g.circle(x, y, int(S/80), S, S,c)

passed = 0
sAC = 360/60
msAC = sAC/1000000
mAC = 360/60
hAC = 360/12
change = True
t = datetime.datetime.now()
lastsecondANGLE = secondANGLE
lastminuteANGLE = minuteANGLE
lasthourANGLE = hourANGLE
secondANGLE = (t.second * sAC) + (t.microsecond * msAC)
minuteANGLE = t.minute * mAC
hourANGLE = t.hour * hAC

while True:
    while not change:
        t = datetime.datetime.now()
        lastsecondANGLE = secondANGLE
        lastminuteANGLE = minuteANGLE
        lasthourANGLE = hourANGLE
        secondANGLE = (t.second * sAC) + (t.microsecond * msAC)
        minuteANGLE = t.minute * mAC
        hourANGLE = t.hour * hAC
        if lastsecondANGLE!=secondANGLE:
            for i in range(prev,int(secondANGLE)):
                l = math.tsx.get(tsxS, i)
                g.circle(*g.cap(l[0], l[1], S, S), int(S / 90), S, S, g.purple)
            prev = int(secondANGLE)
        if int(lastminuteANGLE)!=int(minuteANGLE):
            change=True
    g.rect(0, 0, S, S, g.black)
    for i in range(360):
        l = math.tsx.get(tsx, i)
        g.circle(*g.cap(l[0], l[1], S, S), int(S / 110), S, S)
    for i in range(int(secondANGLE)):
        l = math.tsx.get(tsxS, i)
        g.circle(*g.cap(l[0], l[1], S, S), int(S / 90), S, S, g.purple)
    # g.line(*g.cap(*middle,S,S),*g.cap(*math.tsx.get(tsxS,int(secondANGLE)),S,S),S,S,g.purple,secondLine)
    g.line(*g.cap(*middle, S, S), *g.cap(*math.tsx.get(tsxM, int(minuteANGLE)), S, S), S, S, g.red, minuteLine)
    g.line(*g.cap(*middle, S, S), *g.cap(*math.tsx.get(tsxH, int(hourANGLE)), S, S), S, S, g.green, hourLine)
    change = False
    prev = 0

input()
g.clear()

input()
