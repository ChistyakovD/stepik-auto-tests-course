from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_100 = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element_by_id('book').click()

    x = browser.find_element_by_id('input_value').text
    y = math.log(abs(12*math.sin(int(x))))

    answer = browser.find_element_by_id('answer').send_keys(str(y))

    button = browser.find_element_by_id('solve').click()



finally:
    time.sleep(10)
    browser.quit()

