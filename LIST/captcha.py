from time import sleep
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
keyboard = KeyboardController()

# Переход в другое окно
def patcha():
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    sleep(0.5)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)
    sleep(0.5)

    # Обновление данных 
    keyboard.press(key=Key.f5)
    sleep(0.5)
    keyboard.release(key=Key.f5)
    sleep(2)

    # нажатие ввод
    keyboard.press(key=Key.enter)
    sleep(0.5)
    keyboard.release(key=Key.enter)
    sleep(2)

    # наведение курсора на ячейку и нажатие кнопки мыши
    # окно 80% в Chrome
    mouse.position = (71, 286)
    mouse.press(Button.left)
    sleep(0.5)
    mouse.release(Button.left)
    sleep(2)

    # наведение на кнопку и нажатие 
    mouse.position = (103, 369)
    mouse.press(Button.left)
    sleep(0.5)
    mouse.release(Button.left)
    sleep(2)

    # нажатие переход в окно 
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    sleep(0.5)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)

    # нажатие ввод
    mouse.position = (679, 466)
    mouse.press(Button.left)
    sleep(0.5)
    mouse.release(Button.left)
    sleep(0.5)
    keyboard.press(key=Key.enter)
    sleep(0.5)
    keyboard.release(key=Key.enter)



