from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    browser.find_element_by_css_selector(".btn-primary").click()
    browser.switch_to.alert.accept()

    x_element = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(x_element))

    browser.find_element_by_css_selector(".btn-primary").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла