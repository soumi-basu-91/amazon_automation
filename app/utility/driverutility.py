import platform

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from app.utility.baseutility import Baseutility


class Driverutility(Baseutility):
    def spawn_driver(self, headless_status):
        driver = None
        try:
            driver_path = None
            if platform.system().lower() == "darwin":
                driver_path = super().read_config("browser_config", "mac_chromedriver")
            if platform.system().lower() == "linux":
                driver_path = super().read_config("browser_config", "linux_chromedriver")
            if platform.system().lower() == "windows":
                driver_path = super().read_config("browser_config", "windows_chromedriver")
            if headless_status:
                chrome_options = Options()
                chrome_options.add_argument('--disable-blink-features=AutomationControlled')
                super().set_log("info", "Add option to devoid bot")
                chrome_options.add_argument("--headless")
                super().set_log("info", "set headless argument")
                chrome_options.add_argument("--no-sandbox")
                super().set_log("info", "deactivate sandbox")
                chrome_options.add_argument('--disable-dev-shm-usage')
                super().set_log("info", "deactivate shared virtual memory")
                driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
                driver.implicitly_wait(10)
                super().set_log("info", "Adding implicit wait time")
                super().set_windowsize(driver, 1080, 1920)
                super().set_log("info", "web driver intialized for chrome")
            else:
                super().set_log("info", "Setting driver path to " + driver_path)
                chrome_options = Options()
                chrome_options.add_argument('--disable-blink-features=AutomationControlled')
                super().set_log("info", "Add option to devoid bot")
                driver = webdriver.Chrome(executable_path=driver_path)
                driver.implicitly_wait(10)
                super().set_log("info", "Adding implicit wait time")
                driver.maximize_window()
                super().set_log("info", "Maximize window")
                super().set_log("info", "web driver initialized for chrome")
        except WebDriverException as e:
            super().set_log("error", e)

        return driver
