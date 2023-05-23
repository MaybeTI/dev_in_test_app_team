from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Union


class Page:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(
        self,
        by: Union[str, MobileBy] = MobileBy.ID,
        link: str = None,
        many: bool = False,
    ) -> Union[WebElement, List[WebElement]]:
        locator = (by, link)
        if many:
            return self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(
        self,
        by: Union[str, MobileBy] = MobileBy.ID,
        link: str = None,
    ) -> None:
        self.find_element(by, link).click()

    def send_keys(
        self,
        by: Union[str, MobileBy],
        link: str = None,
        many: bool = False,
        *args: str,
    ) -> None:
        elements = self.find_element(by, link, many)
        if many:
            for index, element in enumerate(elements):
                element.send_keys(args[index])
            return
        elements.send_keys(*args)
