from time import sleep
from wsgiref import headers
import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup
import test
import test.test_html

#TODO открыть все ссылки на CRM и сохранить из них ИНН
#Тестируем на 1 странице
all_links = []

for i in range(1,79):
    with open(f'CRM_download/Data/region_pages{i}.html', "r", encoding='utf-8') as f:        
        data = f.read()
    soup = BeautifulSoup(data, "lxml")

    link = soup.find("div",class_="form-group").find_all("a",class_="nav-link")
    for link in link:
        all_links.append(link.get("href")+"\n") 

with open('CRM_download/all_links.txt', "w", encoding='utf-8') as f:        
     f.write(str(all_links))

# # сохраняем в файл
# with open('CRM_download/test.html', "w", encoding='utf-8') as f:        
#     f.write(page.text)

#TODO сохранить в файл 