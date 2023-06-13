from typing import Tuple, Union, Any

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver, Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from testing.settings import testing_settings


class BaseSeleniumTestCase(StaticLiveServerTestCase):
    approve_delete_button_locator = (By.CSS_SELECTOR, 'input[type=submit][value="Yes, I’m sure"]')

    def setUp(self) -> None:
        options = Options()

        if testing_settings['RUN_TESTS_IN_HEADLESS_MODE']:
            options.add_argument('--headless')

        self.browser = WebDriver(options=options)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, testing_settings['TIMEOUT'])
        self.addCleanup(self.browser.quit)

    def open_page(self, url: str) -> None:
        self.browser.get(self.build_absolute_url(url))

    def build_absolute_url(self, url: str) -> str:
        if url.startswith('http'):
            return url
        elif url.startswith('/'):
            return f'{self.live_server_url}{url}'
        else:
            return f'{self.live_server_url}/{url}'

    # def assertPageChanged(self, desired_page_url: str, msg: str = None) -> None:
    #     msg = msg or f'Page has not been changed to {desired_page_url}.'
    #     self.assertTrue(self.wait.until(ec.url_to_be(desired_page_url)), msg)

    def assertElementIsVisible(self, locator: Union[Tuple, WebElement, str], msg: str = None) -> None:
        try:
            if len(locator) <= 2:
                self.wait.until(ec.visibility_of_element_located(locator))
            else:
                self.wait.until(
                    ec.visibility_of_element_located(locator[:2]), f'{locator[2]} is not presented or not visible.'
                )
        except TimeoutException:
            raise self.failureException(msg or 'Element is not present or not visible.')

    # def assertElementIsInvisible(self, locator: Union[Tuple, WebElement, str], msg: str = None) -> None:
    #     try:
    #         if len(locator) <= 2:
    #             self.wait.until_not(ec.visibility_of_element_located(locator))
    #         else:
    #             self.wait.until_not(
    #                 ec.visibility_of_element_located(locator[:2]), f'{locator[2]} should be invisible or not presented.'
    #             )
    #     except TimeoutException:
    #         raise self.failureException(msg or 'Element is still visible.')
    #
    # def assertElementHasText(self, locator: Union[Tuple, WebElement, str], expected_text: str) -> None:
    #     self.assertEquals(self.find_element(locator).text, expected_text)

    def find_element(self, locator: Union[Tuple, WebElement, str]) -> WebElement:
        if isinstance(locator, tuple):
            return self.browser.find_element(*locator[:2])
        elif isinstance(locator, WebElement):
            return locator
        elif isinstance(locator, str):
            return self.browser.find_element(By.CSS_SELECTOR, locator)
        else:
            raise ValueError('locator should be an instance of tuple, string or WebElement types.')

    def change_select_value(self, select_locator: Union[Tuple, WebElement, str], value: Any) -> None:
        select = Select(self.find_element(select_locator))
        select.select_by_value(str(value))

    # def assertSelectHasValue(self, select_locator: Union[Tuple, WebElement, str], value: Any) -> None:
    #     select = Select(self.find_element(select_locator))
    #     selected_option = select.first_selected_option
    #
    #     self.assertEquals(selected_option.get_attribute('value'), str(value))

    def change_input_value(self, locator: Union[Tuple, WebElement, str], value: Any) -> None:
        element = self.find_element(locator)
        element.clear()
        element.send_keys(str(value))

    # def click_checkbox(self, locator: Union[Tuple, WebElement, str]) -> None:
    #     element = self.find_element(locator)
    #     element.click()
    #
    # def assertCheckboxIsSelected(self, locator: Union[Tuple, WebElement, str]) -> None:
    #     checkbox = self.find_element(locator)
    #     checkbox_selected = checkbox.is_selected()
    #
    #     self.assertTrue(checkbox_selected)

    def click_approve_delete_button(self) -> None:
        approve_delete_button = self.find_element(self.approve_delete_button_locator)
        approve_delete_button.click()
