from time import sleep
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
keyboard = KeyboardController()

# Переход в другое окно
def patcha(place):
    
    """Нажатие на чек бокс и переход на ввод"""
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

    # наведение курсора на чек бокс и нажатие кнопки мыши
    # окно 80% в Chrome
    if place == 'Mega':
        mouse.position = (71, 286) # Для Мега компа
    if place == 'Home':
        mouse.position = (61, 333) # Для домашнего компа
    
    mouse.press(Button.left)
    sleep(0.5)
    mouse.release(Button.left)
    sleep(2)

    # наведение на кнопку "Проверить!" и нажатие 
    if place == 'Mega':
        mouse.position = (114, 348) # Для Мега компа 
    if place == 'Home':
        mouse.position = (100,437) # Для домашнего компа 
    
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
    # mouse.position = (679, 466)
    # mouse.press(Button.left)
    # sleep(0.5)
    # mouse.release(Button.left)
    # sleep(0.5)
    # keyboard.press(key=Key.enter)
    # sleep(0.5)
    # keyboard.release(key=Key.r)


if __name__ == "__main__":
    patcha(place='Home')