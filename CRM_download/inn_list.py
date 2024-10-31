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

#открыть все ссылки на CRM и сохранить из них ИНН
#Тестируем на 1 странице
inn_list = ["INN"]

for i in range(1,2):
    with open(f'CRM_download/Data/region_pages{i}.html', "r", encoding='utf-8') as f:        
        data = f.read()
    soup = BeautifulSoup(data, "lxml")
    items = soup.find_all("tr")
    for item in items:
        inn = item.find("td")
        # print(inn)

# for link in link:
#     all_links.append(link.get("href")) 

# df = pd.DataFrame(all_links)
# df.to_csv('CRM_download/links.csv', index=False)

# # сохраняем в файл
# with open('CRM_download/test.html', "w", encoding='utf-8') as f:        
#     f.write(page.text)

#TODO сохранить в файл 