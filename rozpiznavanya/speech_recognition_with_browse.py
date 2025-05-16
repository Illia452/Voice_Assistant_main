import undetected_chromedriver as uc
import time
import random
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import win32gui
from pywinauto import Application
import pygetwindow as gw


def delay():
    time.sleep(random.uniform(2, 4))


load_dotenv("secret_data/inf.env")
unique_title = "MySupereWindow_12345"
options = uc.ChromeOptions()

options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--allow-file-access-from-files")
options.add_argument("--use-fake-device-for-media-stream")

driver = uc.Chrome(options=options)
# driver.set_window_position(10000, 100)
driver.get(f"data:text/html,<title>{unique_title}</title>")



# 3. Знаходимо вікно по заголовку
window = gw.getWindowsWithTitle(unique_title)[0]
hwnd = window._hWnd
print(f"HWND: {hwnd}")

# 4. Підключаємось до цього вікна через PyWinAuto
app = Application(backend="win32").connect(handle=hwnd)
win = app.window(handle=hwnd).wrapper_object()
win.set_focus()


delay()
delay()

# === 6. Переміщаємо вікно за межі екрана ===
win.move_window(x=-1919, y=0, width=1920, height=1080)

# === 7. Клікаємо по координатах (відносно вікна) ===
# Наприклад, клік по кнопці, яка знаходиться в позиції (200, 300)
time.sleep(1)
win.click_input(coords=(200, 300))

print("✅ Готово: вікно сховано і клік виконано.")

# -----------------------------------------------------------------------------------------------------------------




delay()
delay()

driver.get("https://google.com")

delay()
delay()
delay()

singin = driver.find_element(By.CLASS_NAME, 'gb_B')
singin.click()

delay()
driver.switch_to.frame("app")

delay()


def safe_click(driver, by, value, timeout=10):
    # Чекаємо, поки елемент з'явиться в DOM
    el = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )
    
    # Скролимо до елемента
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)

    # Робимо клік через JavaScript (навіть якщо елемент частково прихований)
    driver.execute_script("arguments[0].click();", el)

safe_click(driver, By.CLASS_NAME, "tX9u1b")

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


# button_location = pyautogui.locateOnScreen('photo.png', confidence=0.8)

# if button_location:
#     center = pyautogui.center(button_location)
#     pyautogui.click(center)



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

# button_micro = pyautogui.locateOnScreen('photo2.png', confidence=0.8)

# if button_micro:
#     center1 = pyautogui.center(button_micro)
#     pyautogui.click(center1)


voice_button = driver.find_element(By.XPATH, '//*[@id="docs-palette-dictation"]/div[1]/div[3]/div[1]')
voice_button.click()


try:
    time.sleep(120)
except OSError:
    pass