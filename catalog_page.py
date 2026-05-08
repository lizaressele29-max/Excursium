from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)

    def open(self, url):
        self.browser.get(url)
        self.wait_page_loaded()

    def wait_page_loaded(self):
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def get_page_text(self):
        return self.browser.find_element(By.TAG_NAME, "body").text

    def find_clickable_by_text(self, text):
        locator = (
            By.XPATH,
            f"//*[self::a or self::button][contains(normalize-space(.), '{text}')]",
        )
        return self.wait.until(EC.element_to_be_clickable(locator))

    def elements_by_text(self, text):
        return self.browser.find_elements(
            By.XPATH,
            f"//*[contains(normalize-space(.), '{text}')]",
        )
