import os
from types import NoneType
import pandas as pd
from fileinput import filename
from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep

folder_path = "D:/Download/Контур/"
data_email = []
count = 0
fault = 0
total = len(os.listdir(folder_path))
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_path = os.path.join(folder_path, filename)
        with open(file_path,"r",encoding="utf8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")
            filename = soup.title.text
            full_download = soup.find(class_="_1IKlC")
            if full_download is not None:
                email ='-'
                inn = filename[filename.find("ИНН ")+4:filename.find(", ОГРН")]
                client_name = filename[0:filename.find(",")]
                email_links = soup.find_all(class_="_2DJgz Ps02p")
                for item in email_links:
                    if "@" in item.text:
                        email = item.text
                data_email.append([client_name,inn,email])
                count += 1
            else:
                fault += 1  
            print(f"Загружено - {count}, пустых файлов - {fault}  из {total}, осталось - {total-count-fault}")
# Create a DataFrame from the list
df_email = pd.DataFrame(data_email, columns =['client_name', 'inn', 'email'])
df_email.to_excel('D:/Download/Kontur_email.xlsx', index=True)