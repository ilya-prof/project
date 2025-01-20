from selenium import webdriver

# Запускаем браузер
driver = webdriver.Chrome()

# Переходим на сайт, где нужно сохранить куки

driver.get('https://focus.kontur.ru/entity?query=1027739322082')
i = input("dfsdf")
# Логинимся или выполняем другие действия, после которых сохраняются нужные куки

# Получаем все куки
cookies = driver.get_cookies()

# Сохраняем куки в файл
import json
with open('cookies.json', 'w') as f:
    json.dump(cookies, f)

# Закрываем браузер
driver.quit()

