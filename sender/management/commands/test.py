from django.core.management import BaseCommand
from sender.classes import DutyMessage, HolidayMessage


class Command(BaseCommand):

    def handle(self, *args, **options):

        bot_setting = [2, 'FF00B050', 'FFFF0000']

        dst = 'data.xlsx'

        ms = DutyMessage(dst,
                         bot_setting[0],
                         bot_setting[1],
                         bot_setting[2])
        print(ms.build())

        ms2 = HolidayMessage(dst,
                             bot_setting[0],
                             22,
                             'FF00B0F0'
                             )

        print(ms2.build())
