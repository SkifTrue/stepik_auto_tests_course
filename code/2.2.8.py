# Загрузка файла
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

one = browser.find_element(By.NAME, "firstname")
one.send_keys("Ololo")

two = browser.find_element(By.NAME, "lastname")
two.send_keys("Hahaha")

three = browser.find_element(By.NAME, "email")
three.send_keys("milo")

#time.sleep(10)

# эта конструкция выбирает файл. При условии, что файл находится в одной папке со скриптом
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "name.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(10)
