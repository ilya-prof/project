import datetime
from time import sleep
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup
import requests

count = 0
num=0
data_email = []
begin = datetime.datetime.now()
book = openpyxl.open("book.xlsx")
sheet = book.active
total = sheet.max_row
for row in range(1,sheet.max_row+1):
    email="-"
    url = sheet[row][0].value
    response = requests.get(url)
    response.raise_for_status()
    sleep(2)
    soup = BeautifulSoup(response.text, "lxml")
    filename = soup.title.text

    email_links = soup.find_all(class_="ws-ellipsis contractorCard-ContactItem__text")
    for item in email_links:
        email = "-"
        if "@" in item.text:
            email = item.text
            email = email.strip()
    num += 1
    inn = url.replace("https://saby.ru/profile/", "")
    client_name = filename[0:filename.find("ИНН")-1]
    long = (datetime.datetime.now()-begin)
    long = long.total_seconds()
    print(num, " из ", total,"  Прошло: ",  long, "сек."," ; ", num,". Загружен : ",client_name)  # Output: "Hello, world"
    data_email.append([num,client_name,inn,email])
# # Create a DataFrame from the list

df_email = pd.DataFrame(data_email, columns =['count', 'client_name', 'inn', 'email'])
df_email.to_excel('D:/Download/Sbis_email.xlsx', index=False)
#
# # print ("Обработано - ", " файлов" "за " "секунд)