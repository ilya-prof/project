import string
from time import sleep
from wsgiref import headers
import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup
import test
import test.test_html
import csv
import re
from tqdm import tqdm
import time

#открыть все ссылки на CRM и сохранить из них ИНН
#Тестируем на 1 странице
inn_list = []

for i in tqdm(range(1,84)):  
     time.sleep(0.01)
     with open(f'CRM_download/Data/region_pages{i}.html', "r", encoding='utf-8') as f:        
        data = f.read()
     soup = BeautifulSoup(data, "lxml")
     items = soup.find("div", class_="table-responsive").find_all("tr")
     for item in items:
        try:
            button = item.find("button", class_="btn")
            inn = button["contractorid"]
            inn_list.append(inn)
        except:
            continue    
 
#  сохраняем в файл CSV
df = pd.DataFrame(inn_list)
df.columns = ['INN']
df.to_csv('CRM_download/inn.csv',index=False)
