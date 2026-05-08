from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LandingPage(BasePage):
    URL = "https://excursium.com/"
    CATALOG_URL_PART = "/ekskursii-dlya-shkolnikov/list"

    def open_page(self):
        self.open(self.URL)

    def has_main_content(self):
        text = self.get_page_text()
        return "Экскурси" in text or "экскурс" in text.lower()

    def click_catalog_button(self):
        button = self.find_clickable_by_text("Посмотреть экскурсии")
        button.click()
        self.wait.until(EC.url_contains(self.CATALOG_URL_PART))

    def click_empty_search(self):
        search_buttons = self.browser.find_elements(
            By.XPATH,
            "//*[self::button or self::a]"
            "[contains(normalize-space(.), 'Найти') or contains(normalize-space(.), 'Поиск')]",
        )
        assert search_buttons, "Кнопка поиска не найдена на лендинге"

        search_buttons[0].click()
        self.wait.until(EC.url_contains(self.CATALOG_URL_PART))

    def is_catalog_opened(self):
        return self.CATALOG_URL_PART in self.browser.current_url
