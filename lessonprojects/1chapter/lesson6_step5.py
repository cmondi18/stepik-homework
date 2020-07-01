from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

searchLink = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    # initialise
    browser = webdriver.Chrome()
    browser.get(link)
    # click on searched link
    browser.find_element_by_link_text(searchLink).click()
    # fill the forms
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Denis")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Sivolap")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Novosibirsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла