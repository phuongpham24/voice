from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class VoiceUI():
    def __init__(self, driver, os):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        if os == "android":
            self.voice_entry = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Nói để tạo đơn")]')
            self.voice_input = (AppiumBy.XPATH, "//android.widget.EditText")
        else:
            self.voice_entry = (AppiumBy.XPATH, '//XCUIElementTypeOther[contains(@name, "Nói để tạo đơn")]')
            self.voice_input = (AppiumBy.XPATH, '//XCUIElementTypeTextField')

    def click_voice_entry(self):
        self.element = self.wait.until(EC.presence_of_element_located(self.voice_entry))
        self.element.click()

    def click_voice_input(self):
        self.element = self.wait.until(EC.presence_of_element_located(self.voice_input))
        self.element.click()

    def get_voice_text(self):
        self.element = self.wait.until(EC.presence_of_element_located(self.voice_input))
        self.voice_text = self.element.text
        return self.voice_text