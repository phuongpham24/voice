from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class VoiceUI():
    def __init__(self, driver, os):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)
        if os == "android":
            self.voice_entry = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Nói để tạo đơn")]')
            self.voice_input = (AppiumBy.XPATH, "//android.widget.EditText")
        else:
            self.voice_entry = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Dictate"]')
            self.voice_input = (AppiumBy.XPATH, '//XCUIElementTypeSearchField[@name="MapsSearchTextField"]')

    def click_voice_entry(self):
        # self.element = self.wait.until(EC.presence_of_element_located(self.voice_entry))
        # self.element.click()
        try:
            self.element = self.wait.until(EC.presence_of_element_located(self.voice_entry))
            self.element.click()
            return True
        except (TimeoutException, NoSuchElementException):
            print("Không tìm thấy❌")
            return False

    def click_voice_input(self):
        try:
            self.element = self.wait.until(EC.presence_of_element_located(self.voice_input))
            self.element.click()
            return True
        except (TimeoutException, NoSuchElementException):
            print("Không tìm thấy❌")
            return False

    def get_voice_text(self):
        self.element = self.wait.until(EC.presence_of_element_located(self.voice_input))
        self.voice_text = self.element.text
        return self.voice_text