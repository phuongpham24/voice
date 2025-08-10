from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from test_variables import ANDROID_VINSHOP_CONFIG, IOS_VINSHOP_CONFIG

class App_Connect():
    def __init__(self, os):
        
        self.appium_server_url = "http://localhost:4723"
        if os == "android":
            self.options = UiAutomator2Options()
            self.options.platform_name = ANDROID_VINSHOP_CONFIG["platform_name"]
            self.options.automation_name = ANDROID_VINSHOP_CONFIG["automation_name"]
            self.options.device_name = ANDROID_VINSHOP_CONFIG["device_name"]
            self.options.app_package = ANDROID_VINSHOP_CONFIG["app_package"]
            self.options.app_activity = ANDROID_VINSHOP_CONFIG["app_activity"]
            self.options.language = "en"
            self.options.locale = "US"
            self.options.no_reset = True
        else:
            self.options = XCUITestOptions()
            self.options.platform_name = IOS_VINSHOP_CONFIG["platform_name"]
            self.options.automation_name = IOS_VINSHOP_CONFIG["automation_name"]
            self.options.bundle_id = IOS_VINSHOP_CONFIG["bundle_id"]
            self.options.udid = IOS_VINSHOP_CONFIG["udid"]

    def open_app(self):
        self.driver = webdriver.Remote(self.appium_server_url, options=self.options)
        return self.driver

    def wait(self):
        return WebDriverWait(self.driver, 15)
    
    def teardown(self):
        if self.driver:
            self.driver.quit()
            
    def terminate_app(self):
        self.driver.terminate_app("com.vingroup.VinIDMerchantApp")
