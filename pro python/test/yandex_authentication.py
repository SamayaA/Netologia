from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time

class YaAuth:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://passport.yandex.ru/auth/add")
    
    def authentication(self, login, password):
        try:
            log = self.driver.find_element_by_name("login")
            log.send_keys(login)
            self.driver.find_element_by_tag_name('button').click()
            time.sleep(1)
            wait = WebDriverWait(self.driver, 2)
            wait.until(lambda driver: driver.current_url != "https://passport.yandex.ru/auth/add")
            psswrd = self.driver.find_element_by_name("passwd")
            psswrd.send_keys(password)
            self.driver.find_element_by_id('passp:sign-in').click()
            time.sleep(5)
            self.driver.close()
            return None
        except:
            return "error"
