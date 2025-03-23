import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browse = webdriver.Chrome()

browse.get("https://github.com/Illia452/Voice_Assistant_main")

time.sleep(5)
browse.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(1)
emeil = browse.find_element(By.ID, "login_field")
emeil.click()
emeil.send_keys("whebcjehhcbwj")


# browse.find_element(By.CLASS_NAME, "Button-label").click()

time.sleep(10000)