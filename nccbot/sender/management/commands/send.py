""" Create SuperUser """

import os

from django.core.management import BaseCommand

#from sender.models import BotSetting


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(f'it"s works {args}')
