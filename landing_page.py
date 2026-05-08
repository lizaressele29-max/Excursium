from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CatalogPage(BasePage):
    URL = "https://excursium.com/ekskursii-dlya-shkolnikov/list"

    def open_page(self):
        self.open(self.URL)

    def has_catalog_content(self):
        text = self.get_page_text()
        return "Каталог экскурсий" in text and "Фильтр" in text

    def has_filter_title(self, title):
        return len(self.elements_by_text(title)) > 0

    def show_more_buttons(self):
        return self.browser.find_elements(
            By.XPATH,
            "//*[self::button or self::a][contains(normalize-space(.), 'Показать больше')]",
        )

    def click_first_show_more(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[self::button or self::a]"
                    "[contains(normalize-space(.), 'Показать больше')]",
                )
            )
        )
        before = self.get_page_text()
        button.click()
        self.wait.until(
            lambda driver: driver.find_element(By.TAG_NAME, "body").text != before
            or "Показать меньше" in driver.find_element(By.TAG_NAME, "body").text
        )
        return before, self.get_page_text()

    def has_invalid_price_range(self):
        return "5500₽ - 0₽" in self.get_page_text()

    def has_broken_show_more_text(self):
        return "Показать больше меньше" in self.get_page_text()
