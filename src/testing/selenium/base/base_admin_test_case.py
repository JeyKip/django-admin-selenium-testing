from typing import Tuple, List, Union, Type

from django.db.models import Model
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from testing.settings import testing_settings
from .base_selenium_test_case import BaseSeleniumTestCase


class BaseAdminTestCase(BaseSeleniumTestCase):
    model_cls = None

    def login(self, username: str, password: str) -> None:
        self.open_page(testing_settings['ADMIN_LOGIN_RELATIVE_PATH'])

        username_input = self.find_element((By.ID, 'id_username'))
        username_input.send_keys(username)

        password_input = self.find_element((By.ID, 'id_password'))
        password_input.send_keys(password)

        submit = self.find_element((By.CSS_SELECTOR, '[type=submit]'))
        submit.click()

    # def assertUserRedirectedToChangePage(self, obj_id: int) -> None:
    #     self.assertPageChanged(self.get_change_page_url(obj_id), 'User has not been redirected to the change page.')

    def assertContainerHasLinks(self, locator: Union[Tuple, WebElement, str], links: List[Tuple[str, str]]) -> None:
        container = self.find_element(locator)
        link_elements = container.find_elements(By.TAG_NAME, 'a')

        for (text, href) in links:
            target_link_elements = [
                link for link in link_elements
                if link.text == text and link.get_attribute('href') == self.build_absolute_url(href)
            ]
            if not target_link_elements:
                raise self.failureException(f'Container does not have {text} {href} link.')

    def assertContainerHasImages(self, locator: Union[Tuple, WebElement, str], images: List[Tuple[str, str]]) -> None:
        container = self.find_element(locator)
        image_elements = container.find_elements(By.TAG_NAME, 'img')

        for (src, alt) in images:
            target_image_elements = [
                img for img in image_elements
                if img.get_attribute('src') == self.build_absolute_url(src) and img.get_attribute('alt') == alt
            ]
            if not target_image_elements:
                raise self.failureException(f'Container does not have {src} {alt} image.')

    # def get_add_page_url(self) -> str:
    #     return self.build_absolute_url(
    #         reverse(f'admin:{self.model_cls._meta.app_label}_{self.model_cls._meta.model_name}_add')
    #     )
    #
    # def open_add_page(self) -> None:
    #     self.open_page(self.get_add_page_url())
    #
    def get_list_page_url(self) -> str:
        return self.build_absolute_url(
            reverse(f'admin:{self.model_cls._meta.app_label}_{self.model_cls._meta.model_name}_changelist')
        )

    def open_list_page(self) -> None:
        self.open_page(self.get_list_page_url())

    def get_change_page_url(self, obj_id: int, model_cls: Type[Model] = None) -> str:
        model_cls = model_cls or self.model_cls

        return self.build_absolute_url(
            reverse(f'admin:{model_cls._meta.app_label}_{model_cls._meta.model_name}_change', args=[obj_id])
        )

    # def open_change_page(self, obj_id: int) -> None:
    #     self.open_page(self.get_change_page_url(obj_id))
    #
    # def assertUserRedirectedToListPage(self) -> None:
    #     self.assertPageChanged(self.get_list_page_url(), 'User has not been redirected to the list page.')
