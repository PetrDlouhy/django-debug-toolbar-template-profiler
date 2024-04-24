import os

DEBUG = True
APPLICATION_DIR = os.path.dirname(globals()['__file__'])
SECRET_KEY = "foo"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(APPLICATION_DIR, "templates")],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                        "admin_tools.template_loaders.Loader",
                    ],
                ),
            ],
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
            ],
        },
    }
]
