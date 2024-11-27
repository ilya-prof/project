from openpyxl import Workbook
from captcha import patcha
import openpyxl
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import winsound
   
 
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

data_email = []
workbook = openpyxl.load_workbook(r"G:\Мой диск\ПР лизинг\База клиентов\Email\Адреса для скачивания.xlsm", data_only=True)
sheet = workbook["Адреса List"]  
for row in tqdm(range(2, sheet.max_row+1)): # sheet.max_row+1
# Ищем ссылку на страницу компании
    sleep(0.01)
    url_start = sheet.cell(row=row, column=3).value  
    req = requests.get(url_start, headers=headers)
    sleep(1)
    soup=BeautifulSoup(req.text,"lxml")
    try:
        url = "https://www.list-org.com/" + soup.find('div', class_="org_list").find("a").get("href")
    except:
        # winsound.Beep(frequency=1500,duration=1000)
        patcha()
        # sleep(1)
        # input(r"Нужно пройти Каптчу!!! Продолжить???")
        req = requests.get(url_start, headers=headers)
        sleep(1)
        soup=BeautifulSoup(req.text,"lxml")
        url = "https://www.list-org.com" + soup.find('div', class_="org_list").find("a").get("href")
    # Проходим на страницу компании
    req2 = requests.get(url, headers=headers)
    sleep(1)
    soup2 = BeautifulSoup(req2.text,"lxml")
    
    #Находим ИНН, ОГРН и название
    pre_inn = soup2.title.text
    inn = pre_inn[pre_inn.find("ИНН ")+4:].strip()
    client_name = pre_inn[:pre_inn.find(",")].strip() 
        # Находим email
    try:
        email = soup2.find('a', class_="wwbw").get("href").replace('mailto:', "").replace(',',";").strip()
        
    except:
        email = "Нет" 
        
    data_email.append([client_name,inn,email])
    df_email = pd.DataFrame(data_email)
    df_email.to_excel(r'g:\Мой диск\ПР лизинг\База клиентов\Email\List_email.xlsx', index=False)

winsound.Beep(frequency=1500,duration=1000)
print("Готово")





