from typing import List, Dict, Any

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .base_admin_test_case import BaseAdminTestCase


class BaseAdminListTestCase(BaseAdminTestCase):
    result_list_locator = (By.ID, 'result_list')

    result_list_columns_locator = (By.CSS_SELECTOR, 'thead tr th div.text span, thead tr th div.text a')
    result_list_rows_locator = (By.CSS_SELECTOR, 'tbody tr')
    action_locator = (By.NAME, 'action')
    paginator_locator = (By.CSS_SELECTOR, '#changelist-form p.paginator')

    def assertResultListIsShown(self) -> None:
        self.assertElementIsVisible(self.result_list_locator, 'Result list is expected to be shown.')

    # def assertResultListIsNotShown(self) -> None:
    #     self.assertElementIsInvisible(self.result_list_locator, 'Result list is expected to not be shown.')
    #
    # def assertPaginatorHasNoRecordsText(self) -> None:
    #     self.assertPaginatorHasTextForRecords(0)
    #
    def assertPaginatorHasTextForRecords(self, records_number: int) -> None:
        if records_number == 1:
            expected_text = f'1 {self.model_cls._meta.verbose_name}'
        else:
            expected_text = f'{records_number} {self.model_cls._meta.verbose_name_plural}'

        self.assertEquals(self._get_paginator_text(), expected_text)

    def _get_paginator_text(self) -> str:
        return self.find_element(self.paginator_locator).text

    def assertResultListConsistsOfColumns(self, expected_columns: List[str]) -> None:
        named_columns = [col for col in self._find_columns() if col]
        expected_columns = [col.upper() for col in expected_columns]

        self.assertEquals(named_columns, expected_columns)

    def _find_columns(self) -> List[str]:
        result_list = self.find_element(self.result_list_locator)
        result_list_columns = result_list.find_elements(*self.result_list_columns_locator)
        result_list_columns_titles = [el.text.upper() for el in result_list_columns]

        return result_list_columns_titles

    def assertResultListHasRows(self, rows_count: int) -> None:
        result_list = self.find_element(self.result_list_locator)
        result_list_rows = result_list.find_elements(*self.result_list_rows_locator)

        self.assertEquals(len(result_list_rows), rows_count)

    def assertRowHasValues(self, row_number: int, values: Dict[str, Any], full_match: bool = True) -> None:
        expected_row_data = {key.upper(): str(value) for (key, value) in values.items()}
        actual_row_data = self._find_row_values(row_number)

        if full_match is False:
            for key in list(actual_row_data.keys()):
                if key not in expected_row_data:
                    actual_row_data.pop(key)

        self.assertEquals(actual_row_data, expected_row_data)

    def _find_row_values(self, row_number: int) -> Dict[str, str]:
        values = {}

        result_list = self.find_element(self.result_list_locator)
        target_row = result_list.find_elements(*self.result_list_rows_locator)[row_number - 1]

        for column_index, column_name in enumerate(self._find_columns()):
            if column_name:
                column = target_row.find_elements(By.CSS_SELECTOR, 'td,th')[column_index]
                values[column_name.upper()] = column.text

        return values

    def assertRowColumnHasValue(self, row_number: int, column_name: str, value: Any) -> None:
        row_data = self._find_row_values(row_number)
        column_value = row_data[column_name.upper()]

        self.assertEquals(column_value, str(value))

    def assertRowColumnHasLink(self, row_number: int, column_name: str, text: str, href: str) -> None:
        self.assertContainerHasLinks(self._find_row_column(row_number, column_name), [(text, href)])

    def _find_row_column(self, row_number: int, column_name: str) -> WebElement:
        result_list = self.find_element(self.result_list_locator)
        row = result_list.find_elements(*self.result_list_rows_locator)[row_number - 1]
        column_index = self._find_columns().index(column_name.upper())
        column_element = row.find_elements(By.CSS_SELECTOR, 'td,th')[column_index]

        return column_element

    def select_action(self, action: str) -> None:
        self.change_select_value(self.action_locator, action)

    def select_row(self, entry_pk: int) -> None:
        result_list = self.find_element(self.result_list_locator)
        action_checkbox_selector = f"td.action-checkbox > input[type=checkbox][value='{entry_pk}']"
        action_checkbox = result_list.find_element(By.CSS_SELECTOR, action_checkbox_selector)
        action_checkbox.click()

    def click_action_button(self) -> None:
        action_button = self.find_element((By.CSS_SELECTOR, 'button[type=submit][name=index]'))
        action_button.click()

    def click_search_button(self) -> None:
        action_button = self.find_element((By.CSS_SELECTOR, 'input[type=submit][value=Search]'))
        action_button.click()

    def assertRowColumnHasImage(self, row_number: int, column_name: str, src: str, alt: str) -> None:
        self.assertContainerHasImages(self._find_row_column(row_number, column_name), [(src, alt)])

    def assertRowColumnHasYesImage(self, row_number: int, column_name: str) -> None:
        self.assertRowColumnHasImage(row_number, column_name, '/static/admin/img/icon-yes.svg', 'True')

    def assertRowColumnHasNoImage(self, row_number: int, column_name: str):
        self.assertRowColumnHasImage(row_number, column_name, '/static/admin/img/icon-no.svg', 'False')

    def apply_filter(self, column_verbose_name: str, value: str) -> None:
        filters_panel = self.find_element((By.ID, 'changelist-filter'))
        filter_container = filters_panel.find_element(
            By.CSS_SELECTOR, f'details[data-filter-title="{column_verbose_name}"]'
        )
        link = filter_container.find_element(By.XPATH, f'.//a[text()="{value}"]')
        link.click()

    def clear_filter(self):
        try:
            clear_filters_link = self.find_element((By.CSS_SELECTOR, '#changelist-filter #changelist-filter-clear > a'))
        # this is a normal situation when no filters were applied and there is no "clear all filters" link
        except NoSuchElementException:
            pass
        else:
            clear_filters_link.click()

    def change_search_value(self, value: Any) -> None:
        self.change_input_value((By.ID, 'searchbar'), value)
