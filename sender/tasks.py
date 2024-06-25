from time import sleep

import requests
from requests import Timeout, ConnectionError

from rocketchat_API.rocketchat import RocketChat
from celery import shared_task

from sender.classes import DutyMessage, HolidayMessage
from sender.models import BotSetting


@shared_task
def send_message():
    """Отправка уведомлений в rocket"""

    bot_setting = BotSetting.objects.get(pk=1)

    dst = 'data.xlsx'

    # Загружатор
    count = 0
    while count < 5:
        try:
            r = requests.get(bot_setting.file_url, timeout=5)
            if r.status_code == 200:
                with open(dst, 'wb') as f:
                    f.write(r.content)
                break
            else:
                print(f'Ошибка, ответ сервера: {r.status_code}')
        except Timeout:
            print('Ошибка таймаута')
        except ConnectionError:
            print('Ошибка соединения')
        except Exception as e:
            print(f'Не опознанная ошибка: {e}')
        print(f'Попытка: {count + 2}')
        count += 1
        sleep(1)

    # Экземпляр создателя сообщений
    ms = DutyMessage(dst,
                     bot_setting.str_number_for_day,
                     bot_setting.green,
                     bot_setting.red)

    ms2 = HolidayMessage(dst,
                         bot_setting.str_number_for_day,
                         14,
                         'FF00B0F0')

    # Кортеж из 2 сообщений
    data = ms.build()
    data2 = ms2.build()

    # Форматируем
    message = f"""{data[0]};
    {data[1]};"""

    if data2:
        message += """
        тестируемый функционал:
        """
        message += data2

    # Экземпляр API rocket'a
    rocket = RocketChat(auth_token=bot_setting.rocket_token,
                        user_id=bot_setting.rocket_user_id,
                        server_url=bot_setting.rocket_url)
    # Отправляем
    rocket.chat_post_message(message, channel=bot_setting.rocket_channel)
