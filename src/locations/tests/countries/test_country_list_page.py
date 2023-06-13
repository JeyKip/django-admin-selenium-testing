from testing.selenium.base import BaseAdminListPageTestCase, BaseAdminTestCaseSuperuserMixin
from locations.models import Country
from locations.tests.factories import CountryFactory
from users.tests.factories import UserFactory


class CountryListPageTestCase(BaseAdminTestCaseSuperuserMixin, BaseAdminListPageTestCase):
    model_cls = Country

    NAME_FIELD = 'Name'
    ISO_CODE_FIELD = 'ISO Code'
    NUMBER_OF_USERS_FIELD = 'Number of users'

    def test_when_no_countries_created_yet_then_result_list_should_not_be_shown(self):
        self.open_list_page()

        self.assertResultListIsNotShown()
        self.assertPaginatorHasNoRecordsText()

    def test_when_at_least_one_country_created_then_result_list_should_be_shown_with_expected_columns(self):
        country = CountryFactory()

        self.open_list_page()

        self.assertResultListIsShown()
        self.assertResultListHasRows(1)
        self.assertPaginatorHasTextForRecords(1)
        self.assertResultListConsistsOfColumns([
            self.NAME_FIELD,
            self.ISO_CODE_FIELD,
            self.NUMBER_OF_USERS_FIELD,
        ])

    def test_verify_that_name_column_contains_link_to_country_detail_page(self):
        country = CountryFactory()

        self.open_list_page()

        expected_text = country.name
        expected_link = self.get_change_page_url(country.pk)

        self.assertRowColumnHasLink(1, self.NAME_FIELD, expected_text, expected_link)

    def test_verify_that_rows_contain_correct_values(self):
        country_1, country_2, country_3 = CountryFactory.create_batch(3)
        country_2_users = UserFactory.create_batch(2, country=country_2)
        country_3_users = UserFactory.create_batch(3, country=country_3)

        self.open_list_page()

        self.assertRowHasValues(1, {
            self.NAME_FIELD: country_1.name,
            self.ISO_CODE_FIELD: country_1.iso_code,
            self.NUMBER_OF_USERS_FIELD: 0,
        })
        self.assertRowHasValues(2, {
            self.NAME_FIELD: country_2.name,
            self.ISO_CODE_FIELD: country_2.iso_code,
            self.NUMBER_OF_USERS_FIELD: len(country_2_users),
        })
        self.assertRowHasValues(3, {
            self.NAME_FIELD: country_3.name,
            self.ISO_CODE_FIELD: country_3.iso_code,
            self.NUMBER_OF_USERS_FIELD: len(country_3_users),
        })

    def test_verify_that_countries_sorted_by_id_field_in_ascending_order(self):
        country_1, country_2, country_3, country_4 = CountryFactory.create_batch(4)

        self.open_list_page()

        self.assertRowColumnHasValue(1, self.NAME_FIELD, country_1.name)
        self.assertRowColumnHasValue(2, self.NAME_FIELD, country_2.name)
        self.assertRowColumnHasValue(3, self.NAME_FIELD, country_3.name)
        self.assertRowColumnHasValue(4, self.NAME_FIELD, country_4.name)

        self.assertResultListIsShown()
        self.assertResultListHasRows(4)
        self.assertPaginatorHasTextForRecords(4)

    def test_when_user_uses_search_then_only_matched_countries_should_be_shown(self):
        country_1, country_2, country_3 = CountryFactory.create_batch(3)

        search_test_cases = (
            (country_1.name, country_1),
            (country_1.iso_code, country_1),
            (country_2.name, country_2),
            (country_2.iso_code, country_2),
            (country_3.name, country_3),
            (country_3.iso_code, country_3),
        )

        self.open_list_page()

        for search_value, expected_country in search_test_cases:
            with self.subTest(search_value=search_value, expected_country=expected_country.name):
                self.change_search_value(search_value)
                self.click_search_button()

                self.assertResultListHasRows(1)
                self.assertRowColumnHasValue(1, self.NAME_FIELD, expected_country.name)

    def test_when_user_uses_delete_selected_action_then_selected_countries_should_be_deleted(self):
        country_1, country_2, country_3, country_4 = CountryFactory.create_batch(4)

        self.open_list_page()
        self.select_row(country_1.pk)
        self.select_row(country_3.pk)
        self.select_action('delete_selected')
        self.click_action_button()
        self.click_approve_delete_button()

        [existing_country_1, existing_country_2] = Country.objects.order_by('pk')

        self.assertEquals(country_2.pk, existing_country_1.pk)
        self.assertEquals(country_4.pk, existing_country_2.pk)
