from typing import Any, Tuple, Union, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .base_admin_test_case import BaseAdminTestCase


class BaseAdminChangePageTestCase(BaseAdminTestCase):
    pass
    # title_locator = (By.CSS_SELECTOR, '#content > h2')
    # delete_button_locator = (By.CSS_SELECTOR, '.submit-row a.deletelink')
    # button_locator = (By.CSS_SELECTOR, '.submit-row input[type=submit][name={}]')
    # error_note_locator = (By.CSS_SELECTOR, 'p.errornote')
    #
    # @property
    # def change_form_locator(self):
    #     return By.ID, f'{self.model_cls._meta.model_name}_form'
    #
    # def assertInputHasValue(self, locator: Union[Tuple, WebElement, str], value: Any) -> None:
    #     element = self.find_element(locator)
    #     element_value = element.get_attribute('value')
    #
    #     self.assertEquals(element_value, str(value))
    #
    # def assertFieldHasValue(self, field_name: str, value: Any) -> None:
    #     field = self._find_field_element(field_name, 'div > input,textarea,select')
    #     field_value = field.get_attribute('value')
    #
    #     self.assertEquals(field_value, str(value))
    #
    # def assertFieldHasErrors(self, field_name: str, expected_errors: List[str]) -> None:
    #     field_row = self._find_row_for_field(field_name)
    #     errors = self._find_errors(field_row)
    #
    #     self.assertEquals(errors, expected_errors)
    #
    # def assertFieldHasNoErrors(self, field_name: str) -> None:
    #     field_row = self._find_row_for_field(field_name)
    #     errors = self._find_errors(field_row)
    #
    #     self.assertEquals(errors, [])
    #
    # def _find_errors(self, container: WebElement, css_selector='ul.errorlist > li'):
    #     error_elements = container.find_elements(By.CSS_SELECTOR, css_selector)
    #     errors = [element.text for element in error_elements]
    #
    #     return errors
    #
    # def assertPageHasErrors(self, expected_errors: List[str]) -> None:
    #     change_form = self.find_element(self.change_form_locator)
    #     errors = self._find_errors(change_form, 'ul.errorlist.nonfield > li')
    #
    #     self.assertEquals(errors, expected_errors)
    #
    # def assertInlineFormHasErrors(
    #         self, inline_form_locator: Union[Tuple, WebElement, str], expected_errors: List[str]
    # ) -> None:
    #     inline_form = self.find_element(inline_form_locator)
    #     errors = self._find_errors(inline_form, 'fieldset > ul.errorlist > li')
    #
    #     self.assertEquals(errors, expected_errors)
    #
    # def assertFieldHasText(self, field_name: str, expected_text: str) -> None:
    #     field = self._find_field_element(field_name, 'div > div.readonly')
    #
    #     self.assertEquals(field.text, str(expected_text))
    #
    # def _find_field_element(self, field_name: str, css_selector: str) -> WebElement:
    #     field_row = self._find_row_for_field(field_name)
    #     field = field_row.find_element(By.CSS_SELECTOR, css_selector)
    #
    #     return field
    #
    # def _find_row_for_field(self, field_name: str) -> WebElement:
    #     field_index = self._find_field_names().index(field_name)
    #     field_row = self._find_field_rows()[field_index]
    #
    #     return field_row
    #
    # def _find_field_rows(self) -> List[WebElement]:
    #     fields = []
    #
    #     for fieldset in self.browser.find_elements(By.CSS_SELECTOR, 'form > div > fieldset.module'):
    #         fields.extend(fieldset.find_elements(By.CSS_SELECTOR, 'div.form-row:not([style*="display: none"])'))
    #
    #     return fields
    #
    # def assertPageHasFields(self, expected_fields: List[str]) -> None:
    #     self.assertEquals(self._find_field_names(), expected_fields)
    #
    # def _find_field_names(self, required_only: bool = False) -> List[str]:
    #     label_selector = 'div.form-row:not([style*="display: none"]) div > label'
    #
    #     if required_only:
    #         label_selector += '.required'
    #
    #     field_rows = self._find_field_rows()
    #     field_titles = (
    #         label for row in field_rows for label in row.find_elements(By.CSS_SELECTOR, label_selector) if label
    #     )
    #     field_names = [el.text.strip().strip(':') for el in field_titles]
    #
    #     return field_names
    #
    # def assertPageHasRequiredFields(self, expected_fields: List[str]) -> None:
    #     self.assertEquals(self._find_change_page_required_field_names(), expected_fields)
    #
    # def _find_change_page_required_field_names(self) -> List[str]:
    #     return self._find_field_names(required_only=True)
    #
    # def assertFieldIsRequired(self, field_name: str) -> None:
    #     self.assertTrue(field_name in self._find_change_page_required_field_names())
    #
    # def assertTitleHasValue(self, title: str) -> None:
    #     self.assertEquals(self.find_element(self.title_locator).text, title)
    #
    # def assertPageHasDeleteButton(self) -> None:
    #     self.assertElementIsVisible(self.delete_button_locator)
    #
    # def assertPageHasNoDeleteButton(self) -> None:
    #     self.assertElementIsInvisible(self.delete_button_locator)
    #
    # def assertPageHasSaveButton(self) -> None:
    #     self.assertPageHasButton('_save')
    #
    # def assertPageHasNoSaveButton(self) -> None:
    #     self.assertPageHasNoButton('_save')
    #
    # def assertPageHasSaveAndContinueButton(self) -> None:
    #     self.assertPageHasButton('_continue')
    #
    # def assertPageHasNoSaveAndContinueButton(self) -> None:
    #     self.assertPageHasNoButton('_continue')
    #
    # def assertPageHasSaveAndAddAnotherButton(self) -> None:
    #     self.assertPageHasButton('_addanother')
    #
    # def assertPageHasNoSaveAndAddAnotherButton(self) -> None:
    #     self.assertPageHasNoButton('_addanother')
    #
    # def assertPageHasButton(self, name: str) -> None:
    #     self.assertElementIsVisible(self.get_button_selector(name))
    #
    # def assertPageHasNoButton(self, name: str) -> None:
    #     self.assertElementIsInvisible(self.get_button_selector(name))
    #
    # def click_submit_button(self, button_name: str) -> None:
    #     submit_button = self.find_element((By.CSS_SELECTOR, f'.submit-row input[name={button_name}]'))
    #     submit_button.click()
    #
    # def click_save(self) -> None:
    #     self.click_submit_button('_save')
    #
    # def click_save_and_continue(self) -> None:
    #     self.click_submit_button('_continue')
    #
    # def click_delete(self) -> None:
    #     delete_button = self.find_element(self.delete_button_locator)
    #     delete_button.click()
    #
    # def get_button_selector(self, name: str) -> Tuple[str, str]:
    #     by, selector = self.button_locator
    #
    #     return by, selector.format(name)
    #
    # def assertFieldHasLink(self, field_name: str, text: str, href: str) -> None:
    #     link = self._find_field_element(field_name, 'div > div.readonly > a')
    #     link_text = link.text
    #     link_href = link.get_attribute('href')
    #
    #     self.assertTrue(link_text == text and link_href == self.build_absolute_url(href))
    #
    # def assertErrorNoteIsShown(self) -> None:
    #     self.assertElementIsVisible(self.error_note_locator, 'Error note is not shown.')
    #
    # def assertErrorNoteHasMessage(self, expected_message: str) -> None:
    #     error_note = self._get_error_note_element()
    #
    #     self.assertEquals(error_note.text, expected_message)
    #
    # def _get_error_note_element(self) -> WebElement:
    #     change_form = self.find_element(self.change_form_locator)
    #     error_note = change_form.find_element(*self.error_note_locator)
    #
    #     return error_note
    #
    # def assertInlineFormConsistsOfColumns(
    #         self, form_locator: Union[Tuple, WebElement, str], expected_columns: List[str]
    # ) -> None:
    #     inline_form_columns = [col for col in self._find_inline_form_columns(form_locator) if col]
    #     expected_columns = [col.upper() for col in expected_columns]
    #
    #     self.assertEquals(inline_form_columns, expected_columns)
    #
    # def _find_inline_form_columns(self, form_locator: Union[Tuple, WebElement, str]) -> List[str]:
    #     inline_form = self.find_element(form_locator)
    #     columns = inline_form.find_elements(By.CSS_SELECTOR, 'table thead > tr > th')
    #     column_names = [col.text.upper() for col in columns]
    #
    #     return column_names
    #
    # def assertInlineFormHasNRows(self, form_locator: Union[Tuple, WebElement, str], expected_rows_number: int) -> None:
    #     self.assertEquals(self.get_inline_form_rows_count(form_locator), expected_rows_number)
    #
    # def get_inline_form_rows_count(self, form_locator: Union[Tuple, WebElement, str]) -> int:
    #     return self._get_inline_form_hidden_value(form_locator, (By.CSS_SELECTOR, 'input[name*=-TOTAL_FORMS]'))
    #
    # def assertInlineFormHiddenValueHasValue(
    #         self, form_locator: Union[Tuple, WebElement, str], input_locator: Tuple, expected_value: Any
    # ) -> None:
    #     self.assertEquals(self._get_inline_form_hidden_value(form_locator, input_locator), expected_value)
    #
    # def _get_inline_form_hidden_value(self, form_locator: Union[Tuple, WebElement, str], input_locator: Tuple) -> int:
    #     inline_form = self.find_element(form_locator)
    #     inline_form_input = inline_form.find_element(*input_locator)
    #     inline_form_input_value = int(inline_form_input.get_attribute('value'))
    #
    #     return inline_form_input_value
    #
    # def assertInlineFormHasNInitialRows(
    #         self, form_locator: Union[Tuple, WebElement, str], expected_initial_rows_number: int
    # ) -> None:
    #     self.assertInlineFormHiddenValueHasValue(
    #         form_locator, (By.CSS_SELECTOR, 'input[name*=-INITIAL_FORMS]'), expected_initial_rows_number
    #     )
    #
    # def assertInlineFormHasMinRows(
    #         self, form_locator: Union[Tuple, WebElement, str], expected_min_rows_number: int
    # ) -> None:
    #     self.assertInlineFormHiddenValueHasValue(
    #         form_locator, (By.CSS_SELECTOR, 'input[name*=-MIN_NUM_FORMS]'), expected_min_rows_number
    #     )
    #
    # def assertInlineFormHasMaxRows(
    #         self, form_locator: Union[Tuple, WebElement, str], expected_max_rows_number: int
    # ) -> None:
    #     self.assertInlineFormHiddenValueHasValue(
    #         form_locator, (By.CSS_SELECTOR, 'input[name*=-MAX_NUM_FORMS]'), expected_max_rows_number
    #     )
    #
    # def click_add_inline_row(self, form_locator: Union[Tuple, WebElement, str]) -> None:
    #     inline_form = self.find_element(form_locator)
    #     add_row_button = inline_form.find_element(By.CSS_SELECTOR, 'table tr.add-row a')
    #     add_row_button.click()
    #
    # def assertInlineFormRowHasErrors(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, expected_errors: List[str]
    # ) -> None:
    #     target_row = self._find_target_inline_row(form_locator, row_number)
    #     target_row_errors = self._find_errors(target_row)
    #
    #     self.assertEquals(target_row_errors, expected_errors)
    #
    # def assertInlineFormRowHasNoErrors(self, form_locator: Union[Tuple, WebElement, str], row_number: int) -> None:
    #     target_row = self._find_target_inline_row(form_locator, row_number)
    #     target_row_errors = self._find_errors(target_row)
    #
    #     self.assertEquals(target_row_errors, [])
    #
    # def _find_target_inline_row(self, form_locator: Union[Tuple, WebElement, str], row_number: int) -> WebElement:
    #     inline_form = self.find_element(form_locator)
    #
    #     target_row_selector = f'table tbody tr:nth-child({row_number})'
    #     target_row = inline_form.find_element(By.CSS_SELECTOR, target_row_selector)
    #
    #     return target_row
    #
    # def get_inline_form_column_value(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, column_name: str
    # ) -> str:
    #     target_cell = self._find_target_inline_cell(form_locator, row_number, column_name)
    #     cell_input = target_cell.find_element(By.CSS_SELECTOR, 'input,textarea,select')
    #     cell_value = cell_input.get_attribute('value')
    #
    #     return cell_value
    #
    # def assertInlineFormColumnHasLink(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, column_name: str, text: str, href: str
    # ) -> None:
    #     target_cell = self._find_target_inline_cell(form_locator, row_number, column_name)
    #     link = target_cell.find_element(By.CSS_SELECTOR, 'a')
    #     link_text = link.text
    #     link_href = link.get_attribute('href')
    #
    #     self.assertTrue(link_text == str(text) and link_href == self.build_absolute_url(href))
    #
    # def assertInlineFormColumnHasReadonlyValue(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, column_name: str, expected_value: Any
    # ) -> None:
    #     target_cell = self._find_target_inline_cell(form_locator, row_number, column_name)
    #     paragraph = target_cell.find_element(By.CSS_SELECTOR, 'p')
    #
    #     self.assertEquals(paragraph.text, expected_value)
    #
    # def assertInlineFormColumnHasErrors(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int,
    #         column_name: str, expected_errors: List[str]
    # ) -> None:
    #     target_cell = self._find_target_inline_cell(form_locator, row_number, column_name)
    #     target_cell_errors = self._find_errors(target_cell)
    #
    #     self.assertEquals(target_cell_errors, expected_errors)
    #
    # def assertInlineFormColumnHasNoErrors(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, column_name: str
    # ) -> None:
    #     self.assertInlineFormColumnHasErrors(form_locator, row_number, column_name, [])
    #
    # def _find_target_inline_cell(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, column_name: str
    # ) -> WebElement:
    #     inline_form = self.find_element(form_locator)
    #     columns = self._find_inline_form_columns(form_locator)
    #     column_index = columns.index(column_name.upper())
    #
    #     target_cell_selector = f'table tbody tr:nth-child({row_number}) td:nth-child({column_index + 1})'
    #     target_cell = inline_form.find_element(By.CSS_SELECTOR, target_cell_selector)
    #
    #     return target_cell
    #
    # def find_element_in_inline_row(
    #         self, form_locator: Union[Tuple, WebElement, str], row_number: int, column_name: str, element_locator: Tuple
    # ) -> WebElement:
    #     target_cell = self._find_target_inline_cell(form_locator, row_number, column_name)
    #     target_element = target_cell.find_element(*element_locator)
    #
    #     return target_element
    #
    # def click_delete_checkbox_in_inline_row(
    #         self, inline_form_locator: Union[Tuple, WebElement, str], row_number: int
    # ) -> None:
    #     delete_checkbox = self.find_element_in_inline_row(
    #         inline_form_locator, row_number, 'Delete?', (By.CSS_SELECTOR, 'input[type=checkbox]')
    #     )
    #     delete_checkbox.click()
