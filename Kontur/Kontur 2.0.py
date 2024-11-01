import os
import datetime
from types import NoneType
import pandas as pd
from fileinput import filename
from bs4 import BeautifulSoup
import tqdm

folder_path = "D:/Download/Контур/"
data_email = []
for filename in tqdm(range(1,len(os.listdir(folder_path)):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_path = os.path.join(folder_path, filename)
            with open(file_path,"r",encoding="utf8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")
            filename = soup.title.text
            full_download = soup.find(class_="_1IKlC")
            email_links = soup.find_all(class_="_2DJgz Ps02p")
            if full_download is not None:
                inn = filename[filename.find("ИНН ")+4:filename.find(", ОГРН")]
                client_name = filename[0:filename.find(",")]
                for item in email_links:
                    if "@" in item.text:
                        email = item.text
                    else: email = '-'    
                data_email.append([client_name,inn,email])

# Create a DataFrame from the list
df_email = pd.DataFrame(data_email, columns =['client_name', 'inn', 'email'])
df_email.to_excel('D:/Download/Kontur_email.xlsx', index=True)