from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

WAIT_SECONDS = 0.85
FOLDER = "./data/wav-data"

#VINSHOP
IOS_VINSHOP = {
    "app_config": {
            "options": XCUITestOptions,
            "platform_name": "iOS",
            "automation_name": "XCUITest",
            "bundle_id": "com.vingroup.VinIDMerchantApp",
            "udid": "00008110-000A71540E07A01E"
        },
    "result_column": "B",
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
        "device_name": "Live 4",
        "app_package": "com.vingroup.VinIDMerchantApp.QC",
        "app_activity": "com.example.vinid_merchant_app.MainActivity"
    },
    "result_column": "B",
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

#ESHOP
IOS_ESHOP = {
    "app_config": {
            "options": XCUITestOptions,
            "platform_name": "iOS",
            "automation_name": "XCUITest",
            "bundle_id": "com.vingroup.VinIDMerchantApp",
            "udid": "00008110-000A71540E07A01E"
        },
    "result_column": "B",
    "steps": [
        {
            "action": "click",
            "description": "Tap Misa AVA",
            "element": '//XCUIElementTypeImage[@name="MISA AVA"]'
        },
        {
            "action": "click",
            "description": "Tap icon để ghi âm",
            "element": '(//XCUIElementTypeImage)[last()]'
        },
        {
            "action": "voice",
            "description": "Nói"
        },
        {
            "action": "get_text",
            "description": "Lấy text sau khi voice",
            "element": '(//XCUIElementTypeTextField)[last()]'
        }
    ]
}

ANDROID_ESHOP = {
    "app_config": {
        "options": UiAutomator2Options,
        "platform_name": "Android",
        "automation_name": "UiAutomator2",
        "device_name": "emulator-5554",
        "app_package": "vn.com.misa.eshop",
        "app_activity": "vn.com.misa.eshop.MainActivity"
    },
    "result_column": "C",
    "steps": [
        {
            "action": "sleep",
            "description": "Chờ tooltip tự động tắt",
            "second": 5
        },
        {
            "action": "click",
            "description": "Tap Misa AVA",
            "element": '//android.widget.ImageView[@content-desc="MISA AVA"]'
        },
        {
            "action": "click",
            "description": "Tap icon để ghi âm",
            "element": '//android.widget.EditText/android.widget.ImageView'
        },
        {
            "action": "voice",
            "description": "Nói"
        },
        {
            "action": "get_text",
            "description": "Lấy text sau khi voice",
            "element": '(//android.widget.EditText)[last()]'
        }
    ]
}

#KNOTE
# IOS_KNOTE = {
#     "app_config": {
#             "options": XCUITestOptions,
#             "platform_name": "iOS",
#             "automation_name": "XCUITest",
#             "bundle_id": "com.vingroup.VinIDMerchantApp",
#             "udid": "00008110-000A71540E07A01E"
#         },
#     "result_column": "D",
#     "steps": [
#         {
#             "action": "click",
#             "description": "Tap tab Bán hàng trên tab bar",
#             "element": '//XCUIElementTypeImage[@name="Tính tiền AI"]'
#         },
#         {
#             "action": "click",
#             "description": "Tap icon để ghi âm",
#             "element": '(//XCUIElementTypeImage)[3]'
#         },
#         {
#             "action": "voice",
#             "description": "Nói"
#         },
#         {
#             "action": "get_text",
#             "description": "Lấy text sau khi voice",
#             "element": '(//android.widget.EditText)[last()]'
#         }
#     ]
# }

ANDROID_KNOTE = {
    "app_config": {
        "options": UiAutomator2Options,
        "platform_name": "Android",
        "automation_name": "UiAutomator2",
        "device_name": "emulator-5554",
        "app_package": "com.kiotviet.kiotqr",
        "app_activity": "com.kiotviet.kiotqr.MainActivity"
    },
    "result_column": "E",
    "steps": [
        {
            "action": "click",
            "description": "Tap tab Bán hàng trên tab bar",
            "element": '//android.widget.ImageView[@content-desc="Bán hàng"]'
        },
        {
            "action": "click",
            "description": "Tap icon để ghi âm",
            "element": '(//android.widget.ImageView)[last()]'
        },
        {
            "action": "voice",
            "description": "Nói"
        },
        {
            "action": "get_text",
            "description": "Lấy text sau khi voice",
            "element": '(//android.widget.EditText)[last()]'
        }
    ]
}