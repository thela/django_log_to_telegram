import io
import logging
import traceback

import requests


class TelegramFormatter(logging.Formatter):
    """
    an extension of the usual logging.Formatter to simplify transmitted data
    """
    meta_attrs = [
        'REMOTE_ADDR',
        'HOSTNAME',
        'HTTP_REFERER'
    ]
    limit = -1  # default per logging.Formatter is None

    def format(self, record):
        """
        same as logging.Formatter.format, with added reporting of the meta_attrs when found in request.META, and the
        username that generated the Exception
        """
        s = super().format(record)

        s += "\n{attr}: {value}".format(
            attr='USER',
            value=record.request.user
        )
        for attr in self.meta_attrs:
            if attr in record.request.META:
                s += "\n{attr}: {value}".format(
                    attr=attr,
                    value=record.request.META[attr]
                )
        return s

    def formatException(self, ei):
        """
        same as logging.Formatter.formatException except for the limit passed as a variable
        """
        sio = io.StringIO()
        tb = ei[2]

        traceback.print_exception(ei[0], ei[1], tb, self.limit, sio)
        s = sio.getvalue()
        sio.close()
        if s[-1:] == "\n":
            s = s[:-1]
        return s


class AdminTelegramHandler(logging.Handler):
    """An exception log handler that send a short log to a telegram bot.

    """
    api_url = 'https://api.telegram.org/'

    def __init__(self, bot_id, include_html=False, email_backend=None):
        super().__init__()
        self.include_html = include_html
        self.email_backend = email_backend
        self.bot_id = bot_id

        self.bot_url = '{api_url}bot{bot_id}/'.format(
            api_url=self.api_url,
            bot_id=self.bot_id
        )
        self.chat_id = self.get_chat_id()

        self.setFormatter(TelegramFormatter())

    def emit(self, record):
        self.send_message(self.format(record))

    def get_chat_id(self):
        """
        Method to extract chat id from telegram request.
        """
        get_updates_url = '{bot_url}getUpdates'.format(
            bot_url=self.bot_url
        )
        r = requests.get(get_updates_url)
        r_json = r.json()

        if r_json['ok']:
            try:
                chat_id = r_json['result'][0]['message']['chat']['id']
            except IndexError:
                print(r.json())
                raise IndexError('Did you start a chat with your bot?')
        else:
            raise KeyError('the BOT_TOKEN you provided does not seem to be active')

        return chat_id

    def prepare_json_for_answer(self, data):

        json_data = {
            "chat_id": self.chat_id,
            "text": data,
            "parse_mode": 'HTML',
        }

        return json_data

    def send_message(self, message):
        message_url = '{bot_url}sendMessage'.format(
            bot_url=self.bot_url
        )
        prepared_data = self.prepare_json_for_answer(message)
        requests.post(message_url, json=prepared_data)

