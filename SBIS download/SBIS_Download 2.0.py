from time import sleep
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup
import requests
import tqdm

data_email = []

book = openpyxl.open("book.xlsx")
sheet = book.active
for row in tqdm(range(2,sheet.max_row+1)):
    sleep(0.01) 
    url = sheet[row][0].value
    response = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(response.text, "lxml")
    filename = soup.title.text
    email_links = soup.find_all(class_="ws-ellipsis contractorCard-ContactItem__text")
    for item in email_links:
        email = "-"
        if "@" in item.text:
            email = item.text.strip()
            
    inn = url.replace("https://saby.ru/profile/", "")
    client_name = filename[0:filename.find("ИНН")-1]
    
    data_email.append([client_name,inn,email])

# # Create a DataFrame from the list
df_email = pd.DataFrame(data_email, columns =['client_name', 'inn', 'email'])
df_email.to_excel('D:/Download/Sbis_email.xlsx', index=True)
