from pynput import keyboard, mouse

with keyboard.Events() as events:
    for event in events:
         if event.key == keyboard.Key.esc:
             break
         else:
              print(f'Получено событие клавиатуры {event}')