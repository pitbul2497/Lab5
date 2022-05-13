import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://yandex.ru/")

input1 = browser.find_element_by_id("text")
input1.send_keys("Барнаул")


input2 = browser.find_element_by_class_name("search2__button")
input2.click()


