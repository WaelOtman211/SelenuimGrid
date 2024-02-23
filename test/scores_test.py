import concurrent.futures
import time
import unittest
from functools import partial

from infra.browser_wrapper import BrowserWrapper
from logic.scores_page import ScoresPage  # Renamed to reflect new focus


class ScoresTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def test_check_dark_mode(self,browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get("https://www.365scores.com/he")  # Navigate to the 365Scores website
        scores_page = ScoresPage(driver)
        time.sleep(4)
        scores_page.press_cookies_button()

        mode=scores_page.change_to_dark_mode()
        self.assertTrue(mode,"background dose not dark")


    def test_change_language_localization(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get("https://www.365scores.com/he")  # Navigate to the 365Scores website
        scores_page = ScoresPage(driver)
        time.sleep(4)
        scores_page.press_cookies_button()
        scores_page.change_language_flow()
        time.sleep(2)
        expected_title = "365Scores - Livescore, Results, Fixtures, News and Stats"
        self.assertEqual(expected_title, driver.title, "Title does not match expected value")
        driver.quit()

    def test_search_functionality(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get("https://www.365scores.com/he")  # Navigate to the 365Scores website
        scores_page = ScoresPage(driver)
        time.sleep(4)
        scores_page.press_cookies_button()

        # Perform search
        search_query = "ריאל מדריד"  # Modify with your search query
        scores_page.search_for_query(search_query)
        expected_title = "ריאל מדריד: תוצאות לייב, לוח משחקים וטבלאות - 365Scores"
        self.assertEqual(expected_title, driver.title, "Title does not match expected value")

        driver.quit()

    def test_365scores(self, browser_type):
        driver = self.browser.get_driver(browser_type)
        driver.get("https://www.365scores.com/he")  # Navigate to the 365Scores website
        scores_page = ScoresPage(driver)
        time.sleep(4)
        scores_page.press_cookies_button()
        # Verify the page title or other unique elements to confirm you're on the right page
        expected_title = "365Scores"  # Adjust based on the actual title
        self.assertIn(expected_title, driver.title, "Title does not match expected value")
        driver.quit()

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                # Use partial to pass browser_type argument along with test_365scores method
                executor.map(self.test_365scores, self.browser.browser_types)
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                # Use partial to pass browser_type argument along with test_365scores method
                executor.map(self.test_search_functionality, self.browser.browser_types)
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                # Use partial to pass browser_type argument along with test_365scores method
                executor.map(self.test_change_language_localization, self.browser.browser_types)
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                # Use partial to pass browser_type argument along with test_365scores method
                executor.map(self.test_check_dark_mode, self.browser.browser_types)
        else:
            self.test_365scores(self.browser.default_browser.lower())
            self.test_search_functionality(self.browser.default_browser.lower())
            self.test_change_language_localization(self.browser.default_browser.lower())
            self.test_check_dark_mode(self.browser.default_browser.lower())




