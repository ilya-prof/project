import requests
import tkinter as tk

country = str('RUSSIA') 
proxies = {
    'http': '163.198.214.219:8000',
    'https': '163.198.214.219:8000',
}

def get_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
    except:
        ip = requests.get('https://api.ipify.org', proxies=proxies)
    return ip

def print_ip():
    ip = get_ip()
    if '85.234' in ip:
        country = str('RUSSIA')
    else: country= str('Nederland')
    text = f'IP: {ip}\nCountry: {country}'
    root.overrideredirect(True)  # Удаление верхней панели
    root.attributes('-alpha', 0.5)  # Установка прозрачности окна
    label = tk.Label(root, text=text)
    label.pack()

root = tk.Tk()
print_ip()

root.mainloop()
