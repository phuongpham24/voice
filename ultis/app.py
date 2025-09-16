from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from test_variables import ANDROID_VINSHOP_CONFIG, IOS_VINSHOP_CONFIG

class App():
    def __init__(self, app_config):
        self.mapping = [
            "platform_name",
            "automation_name",
            "device_name",
            "app_package",
            "app_activity",
            "bundle_id",
            "udid",
        ]

        self.appium_server_url = "http://localhost:4723"
        self.options = app_config["options"]()

        for key in self.mapping:
            try:
                setattr(self.options, key, app_config[key])
            except KeyError:
                print(f"[WARN] Missing key '{key}' – ignored")
        
        try:
            self.options.no_reset = True
        except Exception:
            pass
            

    def open_app(self):
        self.driver = webdriver.Remote(self.appium_server_url, options=self.options)
        return self.driver

    def wait(self):
        return WebDriverWait(self.driver, 15)
    
    def teardown(self):
        if self.driver:
            self.driver.quit()
            
    def terminate_app(self, app_config):
        try:
            if "app_package" in app_config:
                self.driver.terminate_app(app_config["app_package"])
            elif "bundle_id" in app_config:
                self.driver.terminate_app(app_config["bundle_id"])
            else:
                print("[WARN] Missing 'app_package' or 'bundle_id'")
        except Exception as e:
            print(f"[ERROR] Failed to terminate app: {e}")
        # if os == "android":
        #     self.driver.terminate_app(ANDROID_VINSHOP_CONFIG["app_package"])
        # else:
        #     self.driver.terminate_app(IOS_VINSHOP_CONFIG["bundle_id"])