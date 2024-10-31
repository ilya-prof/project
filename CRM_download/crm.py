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


headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
session = requests.Session()
session.post('https://crm.pr-liz.ru/login', {
     'text': 'UIV',
     'password': 'uRa5',
     'remember': 1,
})

sleep(3)
region = 58 #b[ в цикле будет ... ]
start = 0 #(в цикле шаг 50)
url_path = f'https://crm.pr-liz.ru/journal-pipe?&clientType=cold&region={region}&form=deals&date_start=2018-01-01&date_finish=2024-10-31&message=&start={start}&verHtml=35'

page = requests.get(url=url_path,headers=headers)

# сохраняем в файл
with open('CRM_download/test.html', "w", encoding='utf-8') as f:        
    f.write(page.text)

#TODO сохранить в файл 