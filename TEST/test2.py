from PIL import Image, ImageTk
import tkinter as tk

def print_image(image_path):
    image = Image.open(image_path)
    image = image.resize((200, 200), resample=Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

root = tk.Tk()
print_image('F:/Pyton/project/russia.png')
root.mainloop()

