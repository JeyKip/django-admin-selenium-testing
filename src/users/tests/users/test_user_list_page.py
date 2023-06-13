from dateutil.relativedelta import relativedelta
from django.utils import timezone

from testing.selenium.base import BaseAdminListPageTestCase, BaseAdminTestCaseSuperuserMixin
from users.models import User
from users.tests.factories import UserFactory


class UserListPageTestCase(BaseAdminTestCaseSuperuserMixin, BaseAdminListPageTestCase):
    model_cls = User

    EMAIL_FIELD = 'Email address'
    FIRST_NAME_FIELD = 'First name'
    LAST_NAME_FIELD = 'Last name'
    STAFF_FIELD = 'Staff status'
    ACTIVE_FIELD = 'Active'

    def test_when_no_other_users_then_only_current_user_should_be_shown(self):
        self.open_list_page()

        self.assertResultListIsShown()
        self.assertResultListHasRows(1)
        self.assertPaginatorHasTextForRecords(1)

    def test_verify_that_table_consist_of_expected_fields(self):
        self.open_list_page()

        self.assertResultListConsistsOfColumns([
            self.EMAIL_FIELD,
            self.FIRST_NAME_FIELD,
            self.LAST_NAME_FIELD,
            self.STAFF_FIELD,
            self.ACTIVE_FIELD,
        ])

    def test_verify_that_email_column_contains_link_to_user_detail_page(self):
        self.open_list_page()

        expected_text = self.superuser.email
        expected_link = self.get_change_page_url(self.superuser.pk)

        self.assertRowColumnHasLink(1, self.EMAIL_FIELD, expected_text, expected_link)

    def test_verify_that_first_name_and_last_name_columns_contain_correct_values(self):
        another_user = UserFactory()

        self.open_list_page()

        self.assertRowHasValues(1, {
            self.FIRST_NAME_FIELD: '',
            self.LAST_NAME_FIELD: '',
        }, full_match=False)

        self.assertRowHasValues(2, {
            self.FIRST_NAME_FIELD: another_user.first_name,
            self.LAST_NAME_FIELD: another_user.last_name,
        }, full_match=False)

    def test_verify_that_is_staff_and_is_active_columns_contain_correct_images(self):
        not_active_staff = UserFactory(is_staff=True, is_active=False)
        not_staff_active = UserFactory(is_staff=False, is_active=True)
        not_staff_not_active = UserFactory(is_staff=False, is_active=False)

        self.open_list_page()

        self.assertRowColumnHasYesImage(1, self.STAFF_FIELD)
        self.assertRowColumnHasYesImage(1, self.ACTIVE_FIELD)

        self.assertRowColumnHasYesImage(2, self.STAFF_FIELD)
        self.assertRowColumnHasNoImage(2, self.ACTIVE_FIELD)

        self.assertRowColumnHasNoImage(3, self.STAFF_FIELD)
        self.assertRowColumnHasYesImage(3, self.ACTIVE_FIELD)

        self.assertRowColumnHasNoImage(4, self.STAFF_FIELD)
        self.assertRowColumnHasNoImage(4, self.ACTIVE_FIELD)

    def test_verify_that_users_sorted_by_date_joined_field_in_ascending_order(self):
        third_user = UserFactory(date_joined=timezone.now() - relativedelta(days=1))
        second_user = UserFactory(date_joined=timezone.now() - relativedelta(days=2))
        first_user = UserFactory(date_joined=timezone.now() - relativedelta(days=4))

        self.open_list_page()

        self.assertRowColumnHasValue(1, self.EMAIL_FIELD, first_user.email)
        self.assertRowColumnHasValue(2, self.EMAIL_FIELD, second_user.email)
        self.assertRowColumnHasValue(3, self.EMAIL_FIELD, third_user.email)
        self.assertRowColumnHasValue(4, self.EMAIL_FIELD, self.superuser.email)

        self.assertResultListIsShown()
        self.assertResultListHasRows(4)
        self.assertPaginatorHasTextForRecords(4)

    def test_when_user_uses_search_then_only_matched_users_should_be_shown(self):
        user_1 = UserFactory(first_name='First_name_1', last_name='Last_name_1')
        user_2 = UserFactory(first_name='First_name_2', last_name='Last_name_2')
        user_3 = UserFactory(first_name='First_name_3', last_name='Last_name_3')

        search_test_cases = (
            (user_1.first_name, user_1),
            (user_2.first_name, user_2),
            (user_3.first_name, user_3),
            (user_1.last_name, user_1),
            (user_2.last_name, user_2),
            (user_3.last_name, user_3),
            (user_1.email, user_1),
            (user_2.email, user_2),
            (user_3.email, user_3),
        )

        self.open_list_page()

        for search_value, expected_user in search_test_cases:
            with self.subTest(search_value=search_value, email=expected_user.email):
                self.change_search_value(search_value)
                self.click_search_button()

                self.assertResultListHasRows(1)
                self.assertRowColumnHasValue(1, self.EMAIL_FIELD, expected_user.email)

    def test_when_user_uses_filters_then_only_matched_users_should_be_shown(self):
        not_active_staff = UserFactory(is_staff=True, is_active=False)
        not_staff_active = UserFactory(is_staff=False, is_active=True)
        not_staff_not_active = UserFactory(is_staff=False, is_active=False)

        filter_test_cases = (
            ('staff status', 'All', (self.superuser, not_active_staff, not_staff_active, not_staff_not_active)),
            ('staff status', 'Yes', (self.superuser, not_active_staff)),
            ('staff status', 'No', (not_staff_active, not_staff_not_active)),

            ('superuser status', 'All', (self.superuser, not_active_staff, not_staff_active, not_staff_not_active)),
            ('superuser status', 'Yes', (self.superuser,)),
            ('superuser status', 'No', (not_active_staff, not_staff_active, not_staff_not_active)),

            ('active', 'All', (self.superuser, not_active_staff, not_staff_active, not_staff_not_active)),
            ('active', 'Yes', (self.superuser, not_staff_active)),
            ('active', 'No', (not_active_staff, not_staff_not_active)),
        )

        self.open_list_page()

        for column_verbose_name, filter_value, expected_users in filter_test_cases:
            with self.subTest(column_verbose_name=column_verbose_name, filter_value=filter_value):
                self.apply_filter(column_verbose_name, filter_value)

                self.assertResultListHasRows(len(expected_users))

                for row_index, user in enumerate(expected_users, start=1):
                    self.assertRowColumnHasValue(row_index, self.EMAIL_FIELD, user.email)

                self.clear_filter()

    def test_when_user_uses_delete_selected_action_then_selected_users_should_be_deleted(self):
        user_1, user_2, user_3 = UserFactory.create_batch(3)

        self.open_list_page()
        self.select_row(user_1.pk)
        self.select_row(user_3.pk)
        self.select_action('delete_selected')
        self.click_action_button()
        self.click_approve_delete_button()

        [existing_user_1, existing_user_2] = User.objects.order_by('pk')

        self.assertEquals(self.superuser.pk, existing_user_1.pk)
        self.assertEquals(user_2.pk, existing_user_2.pk)
