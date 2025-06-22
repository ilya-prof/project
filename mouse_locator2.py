from pynput import mouse
from pynput.mouse import Controller

print('Press Ctrl-C to quit.')
while True:
    mouse = Controller()
# Считывание положения указателя
    print(f'Текущее положение указателя: {mouse.position}')