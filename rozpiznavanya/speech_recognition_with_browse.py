import undetected_chromedriver as uc
import time
import random
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

load_dotenv("secret_data/inf.env")

options = uc.ChromeOptions()

driver = uc.Chrome(options=options)
driver.get("https://google.com")

def delay():
    time.sleep(random.uniform(2, 4))

delay()

singin = driver.find_element(By.CLASS_NAME, 'gb_B')
singin.click()

delay()
driver.switch_to.frame("app")

delay()

sin = driver.find_element(By.CLASS_NAME, 'tX9u1b')
sin.click()

delay()

driver.switch_to.default_content()
delay()


singin1 = driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
singin1.click()

delay()

email = driver.find_element(By.ID, 'identifierId')
email.click()
delay()
email.send_keys(os.getenv("EMAIL"))

delay()

next_after_email = driver.find_element(By.ID, 'identifierNext')
next_after_email.click()

delay()

password = driver.find_element(By.NAME, 'Passwd')
password.click()
delay()
password.send_keys(os.getenv("PASSWORD"))


delay()

next_after_password = driver.find_element(By.ID, 'passwordNext')
next_after_password.click()

delay()
delay()


button_location = pyautogui.locateOnScreen('photo.png', confidence=0.8)

if button_location:
    center = pyautogui.center(button_location)
    pyautogui.click(center)



delay()

driver.get("https://docs.google.com/document/d/1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI/edit?tab=t.0")


instruments = driver.find_element(By.ID, 'docs-tools-menu')
instruments.click()


delay()

voice_write = driver.find_element(By.ID, ":9j")
voice_write.click()

delay()

voice_button = driver.find_element(By.XPATH, '//*[@id="docs-palette-dictation"]/div[1]/div[3]/div[1]')
voice_button.click()

delay()
delay()
delay()

voice_button = driver.find_element(By.XPATH, '//*[@id="docs-palette-dictation"]/div[1]/div[3]/div[1]')
voice_button.click()

button_micro = pyautogui.locateOnScreen('photo2.png', confidence=0.8)

if button_micro:
    center1 = pyautogui.center(button_micro)
    pyautogui.click(center1)


voice_button = driver.find_element(By.XPATH, '//*[@id="docs-palette-dictation"]/div[1]/div[3]/div[1]')
voice_button.click()


try:
    time.sleep(120)
except OSError:
    pass