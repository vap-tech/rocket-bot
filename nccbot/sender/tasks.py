from celery import shared_task


@shared_task
def send_message():
    """Отправка уведомлений пользователям в telegram"""
    print('123 ok')
    return f'send msg'
