======================
Django Log to Telegram
======================

This is a simple logger that sends 500 exceptions to a Telegram bot of your choice.

Quick start
-----------

Install django-log-to-telegram:

.. code:: bash

    pip install -e django_log_to_telegram

1. register a bot on Telegram (`with BotFather <https://core.telegram.org/bots#6-botfather>`_), start a chat with it and put
the Api token in settings.py:

.. code:: python

    LOG_TO_TELEGRAM_BOT_TOKEN = '12345678:replace-me-with-real-token'

Different errors will be fired if the BOT_TOKEN is not active or if there is no chat active with it.

2. add the 'django_log_to_telegram' to your INSTALLED_APPS setting:

.. code:: python

    INSTALLED_APPS = [
        ...
        'django_log_to_telegram',
        ...
    ]

3. add the `django_log_to_telegram.log.AdminTelegramHandler` to your app's logging configuration, for example:

.. code:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'telegram_log': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django_log_to_telegram.log.AdminTelegramHandler',
                'bot_token': LOG_TO_TELEGRAM_BOT_TOKEN,
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['telegram_log'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }

if you want to test this logger in a debug environment, just remove the `filters': ['require_debug_false'],` line in the
'handlers' dictionary.

4. Run `python manage.py migrate` to create the django_log_to_telegram models.

#TODO creare un primo modello

If everything went well, you bot will then begin sending messages on 500 exceptions.

There is a *very basic* test app provided in the folder test_app. It is configured to send errors to telegram even with
DEBUG active, so that it can be useful with just a

.. code:: python

    ./manage.py runserver

It does not provide any database configuration, and most of Django basic settings are stripped out, so any use of it
outside the very basic testing of the django_log_to_telegram mechanism is deprecated to say the least.