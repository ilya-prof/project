from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml 
factory_details=[]

for i in range(3,4):
    with open(f'F:/Pyton/project/{i}.html',"r",encoding="utf-8") as data:
        data = data.read()  
  
    soup = BeautifulSoup(data,'lxml')

    client_name = soup.find("div", class_="title-h1").text
    link = soup.find(href = re.compile('http')).get("href").replace('/details','')
    block= soup.find("ul", class_='content-list').findAll('span')
    for i in range(0,len(block),2):
         content_title =block[i].text
         content_descr=block[i+1].text
         factory_details.append([client_name,link,content_title,content_descr])  

print('Готово', factory_details)