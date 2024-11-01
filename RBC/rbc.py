from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import requests
import openpyxl
from tqdm import tqdm
import time

data_list = []

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
# Делаем цикл:
book = openpyxl.open('RBC/book.xlsx')
sheet = book.active
for row in tqdm(range(2,sheet.max_row+1)): #sheet.max_row+1)  
    time.sleep(0.01) 
    url_start = sheet[row][0].value
    
    # Ищем ссылку на страницу компании
    req = requests.get(url_start, headers=headers)
    soup=BeautifulSoup(req.text,"lxml")
    url = soup.find("a", class_="company-name-highlight").get("href")
    sleep(2)

    # Проходим на страницу компании
    try:
        req2 = requests.get(url, headers=headers)
        sleep(2)
        soup2 = BeautifulSoup(req2.text,"lxml")
    except:
        break
    #Находим ИНН, ОГРН и название
    pre_inn = soup2.title.text
    inn = pre_inn[pre_inn.find("ИНН ")+4:pre_inn.find(" — адрес")].strip()
    name = pre_inn[:pre_inn.find(" — ")].strip() 
    ogrn = pre_inn[pre_inn.find("ОГРН")+5:pre_inn.find(",")].strip()
    # Находим email
    contacts = soup2.find_all('span', class_="copy-text")
    for item in contacts:
        if '@' in item.text: 
            email = item.text.strip().lower()
            break
        else:
            email = "Нет"
    
    # Все заводим в список
    data_list.append([name,ogrn,inn,email])
    df_email = pd.DataFrame(data_list, columns =['name','ogrn','inn','email'])
    df_email.to_excel('RBC/RBC_email.xlsx', index=True)
# Create a DataFrame from the list
# df_email = pd.DataFrame(data_list, columns =['name','inn','email'])
# df_email.to_excel('RBC/RBC_email.xlsx', index=True)
