from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    TIMEOUT = 10 # default wait time in sec

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    #---Navigation-------------------------------------------------------------
    def open(selfself, url: str):
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url

    #---Core Element Helpers----------------------------------------------------
    def find(self, locator: tuple):
        """Wait until visible, then return the element."""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message = f"Element not visible: {locator}"
        )

    def find_clickable(self, locator: tuple):
        """Wait until clickable, then return the element."""
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable: {locator}"
        )

    #---Actions-----------------------------------------------------------------
    def is_visible(self, locator: tuple, timeout: int = TIMEOUT) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_url_contains(selfself, partial_url: str) -> bool:
        try:
            self.wait.until(EC.url_contains(partial_url))
            return True
        except TimeoutException:
            return False

