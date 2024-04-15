from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    yan = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)


      
    
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    
    #button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла