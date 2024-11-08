from openpyxl import Workbook
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.chrome.options import Options

o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get("file:///D:/Download/List-Org.html")

text_title = driver.find_element_by_xpath("")
rint (text_title)



# url_start = sheet.cell(row=row, column=3).value  
# req = requests.get(url_start, headers=headers)
# sleep(1)
# soup=BeautifulSoup(req.text,"lxml")
# try:
#     url = "https://www.list-org.com/" + soup.find('div', class_="org_list").find("a").get("href")
# except:
#     input(r"Нужно пройти Каптчу!!! Продолжить???")
#     req = requests.get(url_start, headers=headers)
#     sleep(1)
#     soup=BeautifulSoup(req.text,"lxml")
#     url = "https://www.list-org.com/" + soup.find('div', class_="org_list").find("a").get("href")
# # Проходим на страницу компании
# req2 = requests.get(url, headers=headers)
# sleep(1)
# soup2 = BeautifulSoup(req2.text,"lxml")

# #Находим ИНН, ОГРН и название
# pre_inn = soup2.title.text
# inn = pre_inn[pre_inn.find("ИНН ")+4:].strip()
# client_name = pre_inn[:pre_inn.find(",")].strip() 
#     # Находим email
# try:
#     email = soup2.find('a', class_="wwbw").get("href").replace('mailto:', "").strip()
# except:
#     email = "Нет" 
    
# data_email.append([client_name,inn,email])
# df_email = pd.DataFrame(data_email)
# df_email.to_excel(r'g:\Мой диск\ПР лизинг\База клиентов\Email\List_email.xlsx', index=False)







