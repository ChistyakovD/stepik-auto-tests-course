import math
import time
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    time.sleep(2)
    browser.get(link)


    box_find = browser.find_element_by_tag_name('img')
    x = box_find.get_attribute('valuex')
    y = calc(x)
    print(x)

    answer_find = browser.find_element_by_id('answer')
    answer_find.send_keys(y)

    checkbox_find = browser.find_element_by_id('robotCheckbox')
    checkbox_find.click()


    radiobutton_find = browser.find_element_by_id('robotsRule')
    radiobutton_find.click()

    button1 = browser.find_element_by_class_name('btn')
    button1.click()

finally:

    time.sleep(10)
    browser.quit()