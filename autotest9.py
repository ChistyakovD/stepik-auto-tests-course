from selenium import webdriver
import time
import math

link = 'http://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    x = browser.find_element_by_id('input_value').text
    y = math.log(abs(12*math.sin(int(x))))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))

    i_am_the_robot = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()

    robots_rules = browser.find_element_by_css_selector('[for="robotsRule"]')
    browser.execute_script('return arguments[0].scrollIntoView();', robots_rules)
    robots_rules.click()

    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView();', button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()