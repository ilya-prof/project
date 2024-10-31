# тестируем функцию beatifoulsoup

from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml 
from tqdm import tqdm
import time

path = "Factory_russia/TEST/"

for i in range(1,10):  
     with open(f'{path}{i}.html',"r",encoding="utf-8") as data:
        data = data.read()  
     soup = BeautifulSoup(data,'lxml')
    # Ищем в файле название клиента (будет ключом), ссылку на страницу , тоже будет ключом и ИНН
    #  client_name = soup.find("div", class_="title-h1").text
     link = soup.find(href = re.compile('https')).get("href").replace('/details','')
     #Если нет ИНН, то значение - "Нет данных"   
     try:
         inn = soup.find(text="ИНН").find_next("span").text             
     except:
         inn= "Нет данных"             
     #Добавляем все данные в список
     print(inn)  
     print(link)