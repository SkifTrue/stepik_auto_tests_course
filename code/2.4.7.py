from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    # Ожидание, пока цена не станет $100. Ожидание проверки наличия данного текста в указанном элементе.
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажатие на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    yan = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()

    time.sleep(5)
finally:
    browser.quit()
