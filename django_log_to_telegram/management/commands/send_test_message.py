# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django_log_to_telegram.models import BotData


class Command(BaseCommand):
    def handle(self, *args, **options):

        bds = BotData.objects.all()

        for bd in bds:
            bd.send_test_message()