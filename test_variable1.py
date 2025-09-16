from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

ANDROID_VINSHOP_CONFIG = {
    "platform_name": "Android",
    "automation_name": "UiAutomator2",
    "device_name": "emulator-5554",
    "app_package": "com.vingroup.VinIDMerchantApp.QC",
    "app_activity": "com.example.vinid_merchant_app.MainActivity"
}

IOS_VINSHOP_CONFIG = {
    "platform_name": "iOS",
    "automation_name": "XCUITest",
    "bundle_id": "com.vingroup.VinIDMerchantApp",
    "udid": "00008110-000A71540E07A01E"
}

OS = "android"
WAIT_SECONDS = 0.85
FOLDER = "./data/wav-data"

IOS_VINSHOP = {
    "app_config": {
            "options": XCUITestOptions,
            "platform_name": "iOS",
            "automation_name": "XCUITest",
            "bundle_id": "com.vingroup.VinIDMerchantApp",
            "udid": "00008110-000A71540E07A01E"
        },
    "result_column": "A",
    "steps": [
        {
            "action": "click",
            "description": "Tap voice menu",
            "element": '//XCUIElementTypeOther[contains(@name, "Nói để tạo đơn")]'
        },
        {
            "action": "voice",
            "description": "Nói"
        },
        {
            "action": "get_text",
            "description": "Lấy text sau khi voice",
            "element": '//XCUIElementTypeTextField'
        }
    ]
}

ANDROID_VINSHOP = {
    "app_config": {
        "options": UiAutomator2Options,
        "platform_name": "Android",
        "automation_name": "UiAutomator2",
        "device_name": "emulator-5554",
        "app_package": "com.vingroup.VinIDMerchantApp.QC",
        "app_activity": "com.example.vinid_merchant_app.MainActivity"
    },
    "result_column": "A",
    "steps": [
        {
            "action": "click",
            "description": "Tap voice menu",
            "element": '//android.view.View[contains(@content-desc, "Nói để tạo đơn")]'
        },
        {
            "action": "voice",
            "description": "Nói"
        },
        {
            "action": "get_text",
            "description": "Lấy text sau khi voice",
            "element": '//android.widget.EditText'
        }
    ]
}