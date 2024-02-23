from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from infra.base_page import Base_Page
import time


class ScoresPage(Base_Page):
    SEARCH_INPUT = "//input[@class='main-header-module-desktop-search-input']"
    SEARCH_RESULTS = "//div[@class='search-widget-result-list-container ps ps__rtl']"
    COOKIES_BUTTON = '//button[@id="didomi-notice-agree-button"]'
    SEARCH_BUTTON = "//div[@class='main-header-module-search-widget-dropdown-container']"
    SETTING_BUTTON = "//button[@class='main-header-module-settings-button']"
    CHOOSE_LANGUAGE_BUTTON = "(//div[@class='language-menu_header__rHHQp'])[2]"
    CHOOSE_LANGUAGE_ENGLISH = "(//div[@class='language-menu_item__n4ICI'])[1]"
    SWITCH_TO_DARK_MODE = "(//div[@class='switch-button_container__xSCbF'])[3]"
    DARK_MODE = "(//html)[1]"


    def __init__(self, driver):

        super().__init__(driver)
        self.mode = self._driver.find_element(By.XPATH, self.DARK_MODE)
        self.setting_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SETTING_BUTTON))
        )

    def press_cookies_button(self):
        print("click cookies")

        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()
        time.sleep(3)

    def change_language_flow(self):

        self.setting_button.click()
        time.sleep(2)

        choose_language_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHOOSE_LANGUAGE_BUTTON))
        )
        choose_language_button.click()
        time.sleep(2)
        choose_language_english = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CHOOSE_LANGUAGE_ENGLISH))
        )
        choose_language_english.click()
        time.sleep(2)

    def change_to_dark_mode(self):

        """try:
            close_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.CLOSE_WINDOWS))
            )
            # If the close button is present, click it to close the window
            close_button.click()
            print("Closed the window.")
        except:
            print("The window is not present or not visible.")
            time.sleep(5)"""

        self.setting_button.click()
        time.sleep(2)
        dark_mode = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SWITCH_TO_DARK_MODE))
        )
        dark_mode.click()
        time.sleep(5)
        if self.mode.get_attribute("data-theme") == "dark":
            return True
        return False

        time.sleep(2)

    def search_for_query(self, query):
        search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search_input.send_keys(query)
        time.sleep(2)
        search_input.send_keys(Keys.RETURN)
        time.sleep(3)
