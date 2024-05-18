import urllib
from rocketchat_API.rocketchat import RocketChat
from celery import shared_task

from classes import MessageBuilder
from sender.models import BotSetting


@shared_task
def send_message():
    """Отправка уведомлений в rocket"""

    bot_setting = BotSetting.objects.get(pk=1)

    dst = 'data.xlsx'

    urllib.request.urlretrieve(bot_setting.file_url, dst)

    ms = MessageBuilder(dst,
                        bot_setting.str_number_for_day,
                        bot_setting.green,
                        bot_setting.red)

    rocket = RocketChat(auth_token=bot_setting.rocket_token,
                        user_id=bot_setting.rocket_user_id,
                        server_url=bot_setting.rocket_url)

    data = ms.build()

    message = f"""{data[0]};
    {data[1]};"""

    rocket.chat_post_message(message, channel=bot_setting.rocket_channel)

    print(message, '\n')
    print('в rocket отправлено')
