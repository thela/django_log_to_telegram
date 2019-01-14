from django.db import models


class BotData(models.Model):
    bot_token = models.CharField(max_length=45)
    chat_id = models.CharField(max_length=8)

