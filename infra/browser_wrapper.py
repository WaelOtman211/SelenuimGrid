from selenium import webdriver
from infra.config_handler import ConfigHandler


class BrowserWrapper:
    def __init__(self):
        config_file_path = 'C:/AutomationWithTsahi/seleniumGrid/infra/config.json'
        self.config_handler = ConfigHandler(config_file_path)
        self.grid_enabled = self.config_handler.get_config_value('grid')
        self.serial_enabled = self.config_handler.get_config_value('serial')
        self.browser_types = self.config_handler.get_config_value('browser_types')
        self.default_browser = self.config_handler.get_config_value('browser')
        self.platform = self.config_handler.get_config_value('platform')
        self.hub_url = self.config_handler.get_config_value('hub_url')
        self.url = self.config_handler.get_config_value('url')

    def get_driver(self, browser_type=None):
        if browser_type:
            if browser_type.lower() == 'chrome':
                return webdriver.Chrome()
            elif browser_type.lower() == 'firefox':
                return webdriver.Firefox()
            elif browser_type.lower() == 'edge':
                return webdriver.Edge()
            else:
                return

        if self.grid_enabled and not self.serial_enabled:
            return self.get_remote_driver()
        else:
            return self.get_local_driver()

    def get_remote_driver(self):
        for browser_type in self.browser_types:
            if browser_type.lower() == 'chrome':
                print("open chrome")
                capabilities = webdriver.ChromeOptions()
            elif browser_type.lower() == 'firefox':
                print("open firefox")
                capabilities = webdriver.FirefoxOptions()
            else:
                print("open edge")
                capabilities = webdriver.EdgeOptions()

            capabilities.capabilities['platformName'] = self.platform
            return webdriver.remote(command_executor=self.hub_url, options=capabilities)

    def get_local_driver(self):
        if self.default_browser.lower() == 'chrome':
            return webdriver.Chrome()
        elif self.default_browser.lower() == 'firefox':
            return webdriver.Firefox()
        elif self.default_browser.lower() == 'edge':
            return webdriver.Edge()
        else:
            # Handle other browser types
            return None  # or raise an exception
