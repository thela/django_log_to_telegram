import warnings

from django.db import models

import requests


class BotData(models.Model):

    api_url = 'https://api.telegram.org/'

    bot_token = models.CharField(max_length=45)
    chat_id = models.CharField(max_length=8, blank=True, null=True)

    def bot_url(self):
        return '{api_url}bot{bot_id}/'.format(
            api_url=self.api_url,
            bot_id=self.bot_token
        )

    def test_token(self):
        response = requests.get('{}{}'.format(
            self.bot_url(),
            "getMe"))
        if response.status_code == 200:
            r_json = response.json()
            if 'ok' in r_json and r_json['ok']:
                print(r_json['result'])
                return True
        else:
            print(response.status_code, response.json())

        return False

    def get_chat_id(self):
        """
        Method to extract chat id from telegram request.
        """

        if self.test_token():
            chat_id = None

            get_updates_url = '{bot_url}getUpdates'.format(
                bot_url=self.bot_url()
            )

            r = requests.get(get_updates_url)
            r_json = r.json()
            try:
                chat_id = r_json['result'][0]['message']['chat']['id']
            except IndexError:
                warnings.warn('Did you start a chat with your bot?', RuntimeWarning)

            self.chat_id = chat_id
            self.save()
        else:
            warnings.warn('the BOT_TOKEN you provided does not seem to be active. BOT_TOKEN={}'.format(
                self.bot_token
            ), RuntimeWarning)

