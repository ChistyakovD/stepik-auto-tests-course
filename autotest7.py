from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    num_1 = int(browser.find_element_by_id('num1').text)
    num_2 = int(browser.find_element_by_id('num2').text)
    summ = str(num_1 + num_2)

    select = Select(browser.find_element_by_class_name('custom-select'))
    select.select_by_value(summ)

    button = browser.find_element_by_tag_name('button').click()


finally:

    time.sleep(10)
    browser.quit()