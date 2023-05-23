from appium.webdriver.common.mobileby import MobileBy

from framework import LoginPage


class SidebarPage(LoginPage):
    def sidebar(self, email: str, password: str) -> None:
        self.login(email, password)
        self.click_element(MobileBy.ID, "com.ajaxsystems:id/menuDrawer")
