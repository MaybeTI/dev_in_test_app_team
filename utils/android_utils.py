import subprocess


def get_device_udid():
    output = subprocess.check_output(["adb", "devices"]).decode().split("\n")
    udid = output[1].split("\t")[0]

    return udid


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "10",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": get_device_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
