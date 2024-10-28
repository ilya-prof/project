import pandas as pd
from bs4 import BeautifulSoup

count =0
client_email_list = []
for i in range(1,5):#10786
    path = "C:/Python/russian_factory/data/" + str(i) + ".html"
    with open(path, 'r', encoding="utf8") as f:
        dwdata = f.read() 
    soup = BeautifulSoup(data, "lxml")
    client_page = soup.find_all("div",class_="content-list__descr")
    for item in client_page:
        count += 1
        client_name = soup.title.text
        client_email = item
        client_email_list.append([client_name, client_email])
        print(client_name, client_email)
        print()

        # print(f'Сделано {count} из 10') #+ str(1082*10))
# # Create a DataFrame from the list
# df_client_email = pd.DataFrame(client_email_list, columns =['client_name', 'client_email'])
# df_client_email.to_excel('C:/Python/russian_factory/finish/db_client_email.xlsx')

