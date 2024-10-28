from ftplib import all_errors

from bs4 import BeautifulSoup
import requests

count = 0
num=0

with open('Works.html',"r",encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
emaillinks = soup.find_all(class_="factory-list")
for item in emaillinks:
    print(item)
