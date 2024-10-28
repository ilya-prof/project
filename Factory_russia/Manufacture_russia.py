from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import requests

url_factory_list = []
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
# сделаем цикл потому что в каждой строке есть ссылка на страницу
url = 'https://ru-brightdata.com/blog/how-tos-ru/scrape-dynamic-websites-python'
src = requests.get(url,headers=headers)
src.raise_for_status()
sleep(2)
print(src.status_code)
data = src.text
print (data)
soup = BeautifulSoup(data, "lxml")
all_url_factory = soup.find_all(class_="factory__head")
for item in all_url_factory:
    url_factory = item.get("href")
    print(url_factory)
    url_factory_list.append(url_factory)

print(url_factory_list)
#
#     email_links = soup.find_all(class_="ws-ellipsis contractorCard-ContactItem__text")
#     for item in email_links:
#         email = "-"
#         if "@" in item.text:
#             email = item.text
#             email = email.strip()
#     num += 1
#     inn = url.replace("https://saby.ru/profile/", "")
#     client_name = filename[0:filename.find("ИНН")-1]
#     long = (datetime.datetime.now()-begin)
#     long = long.total_seconds()
#     print(num, " из ", total,"  Прошло: ",  long, "сек."," ; ", num,". Загружен : ",client_name)  # Output: "Hello, world"
#     data_email.append([num,client_name,inn,email])
# # # Create a DataFrame from the list
#
# df_email = pd.DataFrame(data_email, columns =['count', 'client_name', 'inn', 'email'])
# df_email.to_excel('D:/Download/s_email.xlsx', index=False)
# #
# # print ("Обработано - ", " файлов" "за " "секунд)