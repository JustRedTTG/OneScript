import importlib.util
import os
import time
import datetime
from random import randint

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
save = load_internal_module('save.py')

input("Press enter to continue -> ")
g.clear()
terminal.font((1,1))
g.resize((400, 400))

# SCREEN SIZE

print('Loading data...')
resolution, frames, colors = save.load(os.path.realpath(file+'bad_apple_data'))
g.clear()
g.resize((resolution))
terminal.font((2, 2))
g.clear()

# Bad apple

i = 0

# SCREEN

g.line(1, 1, resolution[0], resolution[1], *resolution)
g.line(1, resolution[1], resolution[0], 1, *resolution)

colors_converted = [g.rgb_convert(color)[0] for color in colors]

for frame in frames:
    for line in frame['lines']:
        # Use this to make the playback speed better but skip a few lines making it noisy
        # if randint(0, 2) == 0:
        #     continue
        g.straight_line(line[0], line[1], line[2] - line[0], colors_converted[line[4]])