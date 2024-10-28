from bs4 import BeautifulSoup
import lxml
import requests 


with open ("F:/Pyton/project/1.html","r", encoding='utf-8') as file:
    r = file.read()
soup = BeautifulSoup(r, 'lxml')

email = soup.find("span",class_="content-list__descr")
print(email)