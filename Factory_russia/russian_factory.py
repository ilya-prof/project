import pandas as pd
from bs4 import BeautifulSoup
import lxml
import re
from tqdm import tqdm
import time
 
count = 0
client_email = []

path = "C:/Python/russian_factory/data/" 
for i in  tqdm(range(1,10786)):  #range(1, 10786): 786
    time.sleep(0.01)
    with open(f'{path}{i}.html', 'r', encoding="utf-8") as f:
        data = f.read() 
    soup = BeautifulSoup(data,features="lxml")
    link = soup.find("link").get("href")
    client_name = soup.title.text
    try:
        email = soup.find(href=re.compile("@")).text
    except:
        email = "Нет данных"
    try:
        page = soup.find(href=re.compile("http:")).get("href")
    except:
        page = "Нет данных"
        

    client_email.append([client_name, email,page,link])
# Create a DataFrame from the list
df_client_email = pd.DataFrame(client_email, columns =['client_name', 'email','page','link'])
df_client_email.to_excel('C:/Python/project/db_client_email.xlsx')

