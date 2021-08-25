from app.pages.checkout import Checkout
from time import sleep

class Testcheckout(Checkout):
    def test_checkout(self):
        headless_status = super().read_config("browser_config", "headless_status")
        driver = super().spawn_driver(headless_status)

        site_url = super().read_config("platform", "site")
        driver.get(site_url)

        # Login
        super().platform_login(driver)
        # search product
        super().search_product(driver)
        # Add to cart
        super().add_to_cart(driver)
        # Checkout
        super().checkout(driver)

        sleep(5)

        driver.quit()
