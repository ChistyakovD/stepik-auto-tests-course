from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/redirect_accept.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    button_1 = browser.find_element_by_tag_name('button').click()

    window = browser.window_handles[1]
    browser.switch_to.window(window)

    x = browser.find_element_by_id('input_value').text
    y = math.log(abs(12*math.sin(int(x))))

    answer = browser.find_element_by_id('answer').send_keys(str(y))

    button = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(10)
    browser.quit()