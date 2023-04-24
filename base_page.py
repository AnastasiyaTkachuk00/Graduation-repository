from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from retrying import retry


class BasePage:

    def open_url(self, url):
        self.driver.get(url)

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://zoobazar.by/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_to_default_context(self):
        self.driver.switch_to.default_content()

    def accept_alert(self):
        alert_el = self.driver.switch_to.alert
        alert_el.accept()
        self.switch_to_default_context()

    def dismiss_alert(self):
        alert_el = self.driver.switch_to.alert
        alert_el.dismiss()
        self.switch_to_default_context()

    def send_keys(self, locator, timer=10):
        input_field = WebDriverWait(self.driver, timer).until(
            EC.element_to_be_clickable(locator))
        input_field.send_keys(locator)

    def get_text_from_element(self, locator, timer=10):
        element = self.find_element(locator, timer)
        return element.text

    def switch_to_iframe(self, iframe_locator, timer=10):
        WebDriverWait(self.driver, timer).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

    def fill_and_accept_alert(self, content):
        alert_el = self.driver.switch_to.alert
        alert_el.send_keys(content)
        alert_el.accept()
        self.switch_to_default_context()

    def click_element(self, locator: tuple):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def click_time_element(self, locator: tuple, timer=10):
        return WebDriverWait(self.driver, timer).until(EC.visibility_of_element_located(locator)).click()

    @retry(stop_max_delay=10000)
    def element_click_with_retry(self, locator, timer=30):
        return (
            WebDriverWait(self.driver, timer).until(
                EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}"
            )
        ).click()
