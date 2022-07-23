import os
for file in os.listdir('resources'):
    if os.path.isdir(f'resources\\{file}'):
        continue
    with open(f'resources\\{file}', 'rb') as f:
        data = f.read()
    with open(f'onescript.py:{file}', 'wb') as f:
        f.write(data)