from time import sleep
from wsgiref import headers
import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup
import test
import test.test_html

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

s = requests.Session()
data = {"login":"UIV", "password":"uRa5"}
url = "https://crm.pr-liz.ru/login"
r = s.post(url, data=data)


s.cookies

sleep(7)

url_path = f'https://crm.pr-liz.ru/kontur-focus?verHtml=34'

page = requests.get(url=url_path,headers=headers)
sleep(3)
# сохраняем в файл
with open(r"D:\Phyton\project\CRM_download\test.html", "w", encoding='utf-8') as f:        
    f.write(page.text)
