import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://coub.com/")

input1 = browser.find_element_by_id("q")
input1.send_keys("коты")
