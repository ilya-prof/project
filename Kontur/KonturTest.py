import os
import datetime
from types import NoneType
import pandas as pd
from fileinput import filename
from bs4 import BeautifulSoup

count = 0
num=0
folder_path = "D:/Download/Контур/"
data_client = []
data_email = []
begin = datetime.datetime.now()
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_path = os.path.join(folder_path, filename)
        # print(file_path)
        with open(file_path,"r",encoding="utf8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")
            title = soup.title
            # print(title.text)

            email = "-"
            filename = title.text

            full_download: None
            full_download = soup.find(class_="_1IKlC")
            email_links = soup.find_all(class_="_2DJgz Ps02p")
            if full_download is not None:
                num += 1
                inn = filename[filename.find("ИНН ")+4:filename.find(", ОГРН")]
                client_name = filename[0:filename.find(",")]
                duration = datetime.datetime.now()-begin
                duration = duration.total_seconds()
                print("прошло: ", duration ," сек."," ; ", num,". Загружен : ",client_name)  # Output: "Hello, world"
                for item in email_links:
                    if "@" in item.text:
                        email = item.text
                    # print(count,';',client_name,';',inn,';',item.text)
                data_email.append([num,client_name,inn,email])
# Create a DataFrame from the list

df_email = pd.DataFrame(data_email, columns =['count', 'client_name', 'inn', 'email'])
df_email.to_excel('D:/Download/Kontur_email.xlsx', index=False)
# df_client= pd.DataFrame(data_client, columns =['client_name', 'inn'])
# df_client.to_excel('D:/Download/Kontur_inn.xlsx', index=False)

# print ("Обработано - ", " файлов" "за " "секунд)