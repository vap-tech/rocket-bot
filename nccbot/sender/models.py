from django.db import models


class BotSetting(models.Model):
    file_url = models.URLField(verbose_name='Ссылка на файл с графиком', null=True)
    green = models.CharField(max_length=400, verbose_name='Зелёный в RGB', null=True)
    red = models.CharField(max_length=400, verbose_name='Красный в RGB', null=True)
    str_number_for_day = models.IntegerField(verbose_name='Номер строки с числом', null=True)
    rocket_token = models.CharField(max_length=400, verbose_name='Rocket.chat Token', null=True)
    rocket_user_id = models.CharField(max_length=100, verbose_name='Rocket.chat User ID', null=True)
    rocket_url = models.URLField(verbose_name='Rocket.chat url', null=True)
    rocket_channel = models.CharField(max_length=100, verbose_name='Название канала или группы Rocket.chat', null=True)

    def __str__(self):
        return 'Настройки бота'

    class Meta:
        verbose_name = 'Настройки бота'
        verbose_name_plural = 'Настройки бота'
