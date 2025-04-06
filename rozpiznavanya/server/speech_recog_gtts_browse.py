import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account

load_dotenv("../../secret_data/inf.env") 




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# приховуємо selenium
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

browse = webdriver.Chrome(options=options)

# видаляємо navigator.webdriver
browse.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

browse.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
        Object.defineProperty(navigator, 'platform', {get: () => 'Win32'});
        Object.defineProperty(navigator, 'deviceMemory', {get: () => 8});
        Object.defineProperty(navigator, 'hardwareConcurrency', {get: () => 8});
    """
})


browse.get("https://docs.google.com/document/d/1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI/edit?hl=uk&tab=t.0")

time.sleep(2.5)


email = browse.find_element(By.XPATH, '//*[@id="identifierId"]')
email.click()
email.send_keys(os.getenv("EMAIL"))


time.sleep(0.5)

next = browse.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
next.click()

time.sleep(3)

password = browse.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
email.send_keys(os.getenv("PASSWORD"))

time.sleep(0.5)

next2 = browse.find_element(By.CLASS_NAME, "VfPpkd-RLmnJb")
next2.click()

time.sleep(0.5)

next3 = browse.find_element(By.CLASS_NAME, "VfPpkd-Jh9lGc")
next3.click()

time.sleep(0.5)


instruments = browse.find_element(By.ID, "docs-tools-menu")
instruments.click()
time.sleep(2)
voice_write = browse.find_element(By.ID, ":9k")
voice_write.click()
time.sleep(2)
voice_button = browse.find_element(By.XPATH, '//*[@id="docs-palette-dictation"]/div[1]/div[3]/div[1]')
voice_button.click()

script = """
let elements = document.querySelectorAll('[role="textbox"] div');
let text = "";
elements.forEach(el => text += el.innerText + "\\n");
return text;
"""
text = browse.execute_script(script)  # Використовуй driver, а не browse
print(text)





