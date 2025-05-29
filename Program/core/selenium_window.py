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


class WindowSelenium():

    def __init__(self):
        load_dotenv("../../rozpiznavanya/secret_data/inf.env")
        self.unique_title = "MySupereWindow_12345"
        options = uc.ChromeOptions()

        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument("--allow-file-access-from-files")
        options.add_argument("--use-fake-device-for-media-stream")

        self.driver = uc.Chrome(options=options)

    def delay_lvl1(self):
        time.sleep(random.uniform(2, 4))

    def delay_lvl2(self):
        time.sleep(random.uniform(5, 7))



    def getting_HWMD(self):
    # driver.set_window_position(10000, 100)
        self.driver.get(f"data:text/html,<title>{self.unique_title}</title>")

        # Знаходимо вікно по заголовку
        window = gw.getWindowsWithTitle(self.unique_title)[0]
        hwnd = window._hWnd
        print(f"HWND: {hwnd}")

        # Підключаємось до цього вікна через PyWinAuto
        app = Application(backend="win32").connect(handle=hwnd)
        self.win = app.window(handle=hwnd).wrapper_object()
        self.win.set_focus()

        self.delay_lvl2()

    
    def move_WindowOutsideDisplay(self):
        # Переміщаємо вікно за межі екрана 
        self.win.move_window(x=0, y=0, width=1920, height=1080)

        # Клікаємо по координатах
        # time.sleep(1)
        # self.win.click_input(coords=(200, 300))

        print("вікно сховано")
        self.delay_lvl2()


    def click_to9point(self):
        singin = self.driver.find_element(By.CLASS_NAME, 'gb_B')
        singin.click()
        self.delay_lvl1()
        

    def click_ToWidgetEMAIL(self, driver, by, value, timeout=10):
        self.driver.switch_to.frame("app")
        self.delay_lvl1()
        # Чекаємо, поки елемент з'явиться в DOM
        el = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        # Скролимо до елемента
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        # Робимо клік через js (навіть якщо елемент частково прихований)
        driver.execute_script("arguments[0].click();", el)

        self.driver.switch_to.default_content()
        self.delay_lvl1()

    def click_signin(self):
        singin1 = self.driver.find_element(By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[2]/a')
        singin1.click()
        self.delay_lvl1()

    def click_and_input_Email(self):
        email = self.driver.find_element(By.ID, 'identifierId')
        email.click()
        self.delay_lvl1()

        email.send_keys(os.getenv("EMAIL"))
        self.delay_lvl1()

        next_after_email = self.driver.find_element(By.ID, 'identifierNext')
        next_after_email.click()
        self.delay_lvl1()

    def click_and_input_Password(self):
        password = self.driver.find_element(By.NAME, 'Passwd')
        password.click()
        self.delay_lvl1()

        password.send_keys(os.getenv("PASSWORD"))
        self.delay_lvl1()

        next_after_password = self.driver.find_element(By.ID, 'passwordNext')
        next_after_password.click()
        self.delay_lvl2()


    def openGoogleDocs(self):
        self.delay_lvl1()
        self.driver.get("https://docs.google.com/document/d/1jxQs9DNNV9gKY_9NvsixZlcqe_Sc-LZKlTwWkp8kYbI/edit?tab=t.0")
        self.delay_lvl1()


    def click_Button_Instruments(self):
        instruments = self.driver.find_element(By.ID, 'docs-tools-menu')
        instruments.click()
        self.delay_lvl1()


    def click_Button_VoiceWrite(self):
        voice_write = self.driver.find_element(By.ID, ":9j")
        voice_write.click()
        self.delay_lvl1()


    def click_StartStop_VoiceWrite(self):
        voice_button = self.driver.find_element(By.XPATH, '//*[@id="docs-palette-dictation"]/div[1]/div[3]/div[1]')
        voice_button.click()
        self.delay_lvl2


    def signInAccountGoogle(self):

        self.driver.get("https://google.com")
        self.delay_lvl2()

        self.click_to9point()
        self.click_ToWidgetEMAIL(self.driver, By.CLASS_NAME, "tX9u1b")
        self.click_signin()
        self.click_and_input_Email()
        self.click_and_input_Password()
    
    def work_withGoogleDocs(self):
        self.openGoogleDocs()
        self.click_Button_Instruments()
        self.click_Button_VoiceWrite()
        self.click_StartStop_VoiceWrite()


    def start(self):
        self.getting_HWMD()
        self.move_WindowOutsideDisplay()
        self.signInAccountGoogle()
        self.work_withGoogleDocs()
        
        try:
            time.sleep(120)
        except OSError:
            pass

if __name__ == "__main__":
    window_selenium = WindowSelenium()
    window_selenium.start()
