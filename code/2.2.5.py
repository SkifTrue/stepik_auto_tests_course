# Метод execute_script
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    yan = browser.find_element(By.CSS_SELECTOR, "#answer")
    yan.send_keys(y)

    ty = browser.find_element(By.ID, "robotCheckbox").click()
    #browser.execute_script("return arguments[0].scrollIntoView(true);", ".btn-primary") #прокрутка страницы
    browser.execute_script("window.scrollBy(0, 100);") #прокрутка страницы
    fri = browser.find_element(By.ID, "robotsRule").click()
    
    
    fo = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    
    #button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

