from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class MobileUIInteraction():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def click_element(self, element):
        try:
            self.element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element)))
            self.element.click()
            return True
        except (TimeoutException, NoSuchElementException):
            print("Không tìm thấy❌")
            return False

    def get_element_text(self, element):
        self.element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element)))
        self.voice_text = self.element.text
        return self.voice_text