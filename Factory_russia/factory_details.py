from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml 
from tqdm import tqdm
import time

factory_details=[]
path = "C:/Python/project-1/Factory_russia/TEST/"

for i in  tqdm(range(1,10)):  #range(1, 10786): 786
     time.sleep(0.01)
     with open(f'{path}{i}.html',"r",encoding="utf-8") as data:
        data = data.read()  
     soup = BeautifulSoup(data,'lxml')
    # Ищем в файле название клиента (будет ключом), ссылку на страницу , тоже будет ключом и ИНН
     client_name = soup.find("div", class_="title-h1").text
     link = soup.find(href = re.compile('http')).get("href").replace('/details','')
     #Если нет ИНН, то значение - "Нет данных"   
     try:
         inn = soup.find(text=re.compile("ИНН")).next_element.next_element.text             
     except:
         inn= "Нет данных"             
     #Добавляем все данные в список
     factory_details.append([client_name,link,inn])  

# Create a DataFrame from the list
df_factory_details = pd.DataFrame(factory_details, columns =['client_name','link','inn'])
df_factory_details.to_excel('db_factory_details.xlsx')
