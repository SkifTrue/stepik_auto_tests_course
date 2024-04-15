# Работа с выпадающим списком

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    x_value = float(x)
    y_value = float(y)
    return str(int(x_value) + int(y_value))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/selects1.html" 
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1').text
    y_element = browser.find_element(By.ID, 'num2').text
    
    z = calc(x_element, y_element)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z) 

    ebosh = browser.find_element(By.CSS_SELECTOR, "button").click()

    #print(z)

    time.sleep(5)
finally:
    browser.quit()