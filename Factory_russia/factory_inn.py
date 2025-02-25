# Сайт "Заводы РФ" парсинг из скаченных файлов реквизитов (только ИНН) и данных для связывания данных в таблице с ИНН

from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml 
from tqdm import tqdm
import time

factory_details=[]
path = "D:/Phyton/Data/factory_russia_inn/"

for i in  tqdm(range(1,3632)):  
     time.sleep(0.01)
     with open(f'{path}{i}.html',"r",encoding="utf-8") as data:
        data = data.read()  
     soup = BeautifulSoup(data,'lxml')
    # Ищем в файле название клиента (будет ключом), ссылку на страницу , тоже будет ключом и ИНН
     client_name = soup.find("div", class_="title-h1").text
     link = soup.find(href = re.compile('http')).get("href").replace('/details','')
     #Если нет ИНН, то значение - "Нет данных"   
     try:
         inn = soup.find(string= re.compile("ИНН")).find_next("span").text             
     except:
         inn= "Нет данных"             
     #Добавляем все данные в список
     factory_details.append([client_name,link,inn])  

# Create a DataFrame from the list
df_factory_details = pd.DataFrame(factory_details, columns =['client_name','link','inn'])
df_factory_details.to_excel('Factory_russia/db_factory_details.xlsx')
