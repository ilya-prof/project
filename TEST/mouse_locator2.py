from pynput import mouse
from pynput.mouse import Controller

while True:
    mouse = Controller()
# Считывание положения указателя
    print(f'Текущее положение указателя: {mouse.position}')