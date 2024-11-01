from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import requests
import openpyxl
from tqdm import tqdm

data_list = []

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
# Делаем цикл:
book = openpyxl.open('RBC/book.xlsx')
sheet = book.active
for row in range(2,15): #sheet.max_row+1)
    url_start = sheet[row][0].value
    
    # Ищем ссылку на страницу компании
    req = requests.get(url_start, headers=headers)
    soup=BeautifulSoup(req.text,"lxml")
    url = soup.find("a", class_="company-name-highlight").get("href")
    sleep(1)

    # Проходим на страницу компании
    try:
        req2 = requests.get(url, headers=headers)
        sleep(2)
        soup2 = BeautifulSoup(req2.text,"lxml")
    except:
        break
    #Находим ИНН
    pre_inn = soup2.title.text
    inn = pre_inn[pre_inn.find("ИНН ")+4:pre_inn.find(" — адрес")].strip()
    # Находим email
    contacts = soup2.find_all('span', class_="copy-text")
    for item in contacts:
        if '@' in item.text: 
            email = item.text.strip()
            break
        else:
            email = "Нет"
    sheet[row][3].value = email
    sheet[row][2].value = inn
    print(inn,email)
    # Все заводим в список
    data_list.append([inn,email])
    book.save('RBC/test.xlsx')
# Create a DataFrame from the list
df_email = pd.DataFrame(data_list, columns =['inn','email'])
df_email.to_excel('RBC/RBC_email.xlsx', index=True)
