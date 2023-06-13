from django.contrib.auth import get_user_model

User = get_user_model()


class BaseAdminTestCaseSuperuserMixin:
    """This class allows to define a test case which runs all tests on behalf of a superuser. For this purpose,
    it creates a new superuser before each test run and logs in this user in the admin panel."""

    def setUp(self) -> None:
        super().setUp()

        superuser_name = 'test_superuser@testmail.com'
        superuser_password = 'test_superuser_password'

        # noinspection PyAttributeOutsideInit
        self.superuser = User.objects.create_superuser(email=superuser_name, password=superuser_password)
        self.login(superuser_name, superuser_password)
