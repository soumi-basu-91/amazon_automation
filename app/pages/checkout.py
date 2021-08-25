from app.pageobject.pageobjectinfo import Selectors
from app.utility.driverutility import Driverutility
from app.utility.assertutility import Assertutility
from selenium.webdriver.common.by import By
from time import sleep


class Checkout(Driverutility, Assertutility):
    # Platform login
    def platform_login(self, driver):
        email = super().read_envdata("email")
        password = super().read_envdata("password")
        webelement_email = driver.find_element(By.XPATH, Selectors.EMAIL)
        webelement_email.send_keys(email)
        super().set_log("info", "Enter email")
        driver.find_element(By.XPATH, Selectors.CONTINUE_BUTTON).click()
        weblement_password = driver.find_element(By.XPATH, Selectors.PASSWORD)
        weblement_password.send_keys(password)
        super().set_log("info", "Enter password")
        driver.find_element(By.XPATH, Selectors.SIGNIN_BUTTON).click()
        dashboard_title = super().read_data("assert", "dashboard_title")
        super().check_equals(
            driver.title,
            dashboard_title.get("data"),
            "Actual title: %s and Expected title: %s is different" % (driver.title, dashboard_title.get("data"))
        )
        super().check_element_present(driver, "xpath", Selectors.SEARCH_BOX)
        super().take_screenshot(driver)

    # Search product
    def search_product(self, driver):
        search_input_data = super().read_data("search", "Bag")
        webelement_email = driver.find_element(By.XPATH, Selectors.SEARCH_BOX)
        webelement_email.send_keys(search_input_data.get("search_keyword"))
        driver.find_element(By.XPATH, Selectors.SEARCH_SUBMIT).click()
        super().take_screenshot(driver)

    # Click on selected product to progress for checkout
    def add_to_cart(self, driver):
        driver.find_element(By.XPATH, Selectors.SEARCH_ITEM).click()
        super().switch_window(driver, 1)
        super().check_element_present(driver, "xpath", Selectors.ADD_TO_CART)
        driver.find_element(By.XPATH, Selectors.ADD_TO_CART).click()
        cart_title = super().read_data("assert", "cart_title")
        super().check_equals(
            driver.title,
            cart_title.get("data"),
            "Actual title: %s and Expected title: %s is different" % (driver.title, cart_title.get("data"))
        )
        super().take_screenshot(driver)

    # Checkout item
    def checkout(self, driver):
        driver.find_element(By.XPATH, Selectors.BUY).click()
        delivery_title = super().read_data("assert", "delivery_title")
        super().check_equals(
            driver.title,
            delivery_title.get("data"),
            "Actual title: %s and Expected title: %s is different" % (driver.title, delivery_title.get("data"))
        )

        # Add delivery information
        address_details = super().read_data("customer", "AZ1")

        driver.find_element(By.XPATH, Selectors.FULL_NAME).send_keys(address_details.get("full_name"))
        super().set_log("info", "Enter full name")
        mobile_number = str(address_details.get("mobile_number"))
        driver.find_element(By.XPATH, Selectors.PHONE_NUMBER).send_keys(mobile_number)
        super().set_log("info", "Enter mobile number")
        postal_code = str(address_details.get("pin_code"))
        driver.find_element(By.XPATH, Selectors.POSTAL_CODE).send_keys(postal_code)
        super().set_log("info", "Enter pin code")
        driver.find_element(By.XPATH, Selectors.APARTMENT).send_keys(address_details.get("apartment"))
        super().set_log("info", "Enter apartment")
        driver.find_element(By.XPATH, Selectors.AREA).send_keys(address_details.get("area"))
        super().set_log("info", "Enter area")
        driver.find_element(By.XPATH, Selectors.LANDMARK).send_keys(address_details.get("landmark"))
        super().set_log("info", "Enter landmark")
        state = address_details.get('state')
        super().check_element_present(driver, "xpath", f"//select[@id='address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId']/option[@value='{state}']")
        driver.find_element(By.XPATH, "//span[@id='address-ui-widgets-enterAddressStateOrRegion']").click()
        sleep(4)
        driver.find_element(By.XPATH, f"//ul[@id='1_dropdown_combobox']//*[contains(text(),'{state}')]").click()
        super().set_log("info", "Select state")
        super().take_screenshot(driver)