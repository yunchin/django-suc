DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "tests.testapp.apps.TestAppConfig",
    # 'tests.testapp',
    # 'testapp',
]

USE_TZ = False
SECRET_KEY = 'dummy'
