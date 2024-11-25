from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открытие браузера
driver = webdriver.Chrome()

# Переход на нужную страницу
driver.get("https://www.list-org.com/company/14020211")
sleep(2)
# Нахождение кнопки по CSS-селектору
box = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]')
box.click()
sleep (2)

button = driver.find_element(By.CSS_Selector, "body > div.main > div.content > div > form > input.btn.btn-primary.m-1")
button.click()
sleep (2)