from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def total(x, y):
  return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_number = browser.find_element_by_id("num1").text
    second_number = browser.find_element_by_id("num2").text

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(total(first_number, second_number))

    browser.find_element_by_css_selector(".btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла