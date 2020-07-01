from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Denis")
    browser.find_element_by_name("lastname").send_keys("Sivolap")
    browser.find_element_by_name("email").send_keys("disivolap@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "lesson2_step8_file.txt")

    browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_css_selector(".btn-primary").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла