from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label
import requests
from io import BytesIO

# Скачиваем изображение флага РФ из интернета

# Создание главного окна
root = tk.Tk()
root.title("Флаг Российской Федерации")
root.attributes("-alpha", 0.5)
root.overrideredirect(True)  # Удаление верхней панели

url = "https://upload.wikimedia.org/wikipedia/en/f/f3/Flag_of_Russia.svg"

try:
    response = requests.get(url)
    response.raise_for_status()
    IMAGE_PATH = "F:\\Pyton\\project\\RU.png"   
except:
     # Путь к изображению на вашем компьютере
     IMAGE_PATH = "F:\\Pyton\\project\\NL.png"

# Загружаем изображение с помощью Pillow
try:
    flag_image = Image.open(IMAGE_PATH)
    flag_image.thumbnail((500, 300))  # Изменение размера изображения
    flag_photo = ImageTk.PhotoImage(flag_image)

    # Создаём и отображаем метку с изображением
    label = Label(root, image=flag_photo)
    label.pack(padx=10, pady=10)
except FileNotFoundError:
    label = Label(root, text="Файл изображения не найден")
    label.pack()


# Запуск главного цикла приложения
root.mainloop()
