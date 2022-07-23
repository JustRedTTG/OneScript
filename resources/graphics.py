import os, __main__, threading
from colorama import Fore, Back
from PIL import Image
terminal = __main__.terminal
math = __main__.math
def clear():
    os.system('cls')
def resize(size):
    print(f"\x1b[8;{size[1]};{size[0]*2}t")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
color = ''
red = Fore.RED
cyan = Fore.CYAN
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
black = Fore.BLACK
white = Fore.WHITE
purple = Fore.MAGENTA
def setColor(c):
    global color
    color = c
def cap(x, y, s1, s2):
    return int(max(0,min(x,s1))), int(max(0,min(y,s2)))
def pixel(x, y, c=None):
    global color
    if (c or color) != black:
        print(f'{c or color}\033[{y};{x*2}H██{bcolors.ENDC}')
    else:
        print(f'\033[{y};{x*2}H  ')
def straight_line(x, y, l, c=None):
    global color
    if (c or color) != black:
        s = ''
        for _ in range(l):
            s += '██'
        print(f'{c or color}\033[{y};{x*2}H{s}{bcolors.ENDC}')
    else:
        s = ''
        for _ in range(l):
            s += '  '
        print(f'\033[{y};{x*2}H{s}')
def straight_line_multicolor(x, y, c=None):
    global color
    i = 0
    for cw, chr in c:
        c1 = cw or color
        if c1 != black:
            print(f'{c1}\033[{y};{(x+i)*2}H{chr+chr}{bcolors.ENDC}')
        else:
            print(f'\033[{y};{(x+i)*2}H  ')
        i += 1
def start_threads(*t):
    for item in t:
        item.start()
def rect(sx, sy, w, h, c=None):
    y = sy
    while y < sy+h:
        #t.append(threading.Thread(target=straight_line, args=(sx, y, w, color), daemon=True).start())
        threading.Thread(target=straight_line, args=(sx, y, w, c or color), daemon=True).start()
        y += 1
    #threading.Thread(target=start_threads, args=(t), daemon=True).start()
brig = '█▒░Ñ@#W$9876543210?!abc;:+=-,._ '
brig = brig[::-1]
def rgb_convert(color):
    if len(color)>3:
        b = color[3]/255
        b *= len(brig)-1
        b = int(b)
    else:
        b = len(brig)-1
    return ['\x1B[38;2;{};{};{}m'.format(color[0],color[1],color[2]), brig[b]]
def image(file, sx, sy):
    image = Image.open(file, 'r')
    y = sy
    while y < sy + image.height:
        colors = []
        x = 0
        while x < image.width:
            colors.append( rgb_convert( image.getpixel((x,y-sy)) ) )
            x += 1
        threading.Thread(target=straight_line_multicolor, args=(sx, y, colors), daemon=True).start()
        y += 1

def line(x0,y0,x1,y1,S1,S2, c=None, function=pixel):
    length = math.dist((x0,y0),(x1,y1))
    for i in range(int(length)):
        function(*cap(*math.lerp((x0,y0),(x1,y1),i),S1, S2),c)

def circle(centerX, centerY, radius, S1, S2, c=None):
    x = 0
    y = radius
    m = 5 - 4 * radius
    while x <= y:
        straight_line(*cap(centerX - x, centerY - y, S1,S2), int(x*2), c)
        straight_line(*cap(centerX - y, centerY - x, S1,S2), int(y*2), c)
        straight_line(*cap(centerX - y, centerY + x, S1,S2), int(y*2), c)
        straight_line(*cap(centerX - x, centerY + y, S1,S2), int(x*2), c)
        if m > 0:
            y -= 1
            m -= 8 * y
        x += 1
        m += 8 * x + 4