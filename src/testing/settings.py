from django.conf import settings

USER_SETTINGS = getattr(settings, 'DJANGO_ADMIN_SELENIUM_TESTING', {})

DEFAULTS = {
    'ADMIN_LOGIN_RELATIVE_PATH': '/admin/login',
    'RUN_TESTS_IN_HEADLESS_MODE': True,
    'TIMEOUT': 10,
}

testing_settings = {**DEFAULTS, **USER_SETTINGS}
