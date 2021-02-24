import os
from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    time.sleep(1)

    name = browser.find_element_by_name('firstname')
    name.send_keys('Dima')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Smit')

    email = browser.find_element_by_name('email').send_keys('46732@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    butten_file = browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_tag_name('button').click()

finally:

    time.sleep(10)
    browser.quit()