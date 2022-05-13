import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://google.com/")

input1 = browser.find_element_by_xpath("//input[@name='q']")
input1.send_keys("Барнаул")


input2 = browser.find_element_by_xpath("(//input[@class='gNO89b'])[2]")
input2.click()


