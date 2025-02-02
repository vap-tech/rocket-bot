from django.db import models


class BotSetting(models.Model):
    file_url = models.URLField(verbose_name='Ссылка на файл с графиком', null=True)
    green = models.CharField(max_length=400, verbose_name='Зелёный в RGB', null=True)
    red = models.CharField(max_length=400, verbose_name='Красный в RGB', null=True)
    blue = models.CharField(max_length=400, verbose_name="Синий в RGB", null=True)
    interval = models.IntegerField(verbose_name="Интервал для отпуска", null=True)
    str_number_for_day = models.IntegerField(verbose_name='Номер строки с числом', null=True)
    col_number_for_nic = models.CharField(verbose_name='Буква столбца с ФИО(регистр не важен)', max_length=2, null=True)
    rocket_token = models.CharField(max_length=400, verbose_name='Rocket.chat Token', null=True)
    rocket_user_id = models.CharField(max_length=100, verbose_name='Rocket.chat User ID', null=True)
    rocket_url = models.URLField(verbose_name='Rocket.chat url', null=True)
    rocket_channel = models.CharField(max_length=100, verbose_name='Название канала или группы Rocket.chat', null=True)

    def __str__(self):
        return 'Настройки бота'

    class Meta:
        verbose_name = 'Настройки бота'
        verbose_name_plural = 'Настройки бота'


class NicOnSurname(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия', null=True)
    nic = models.CharField(max_length=100, verbose_name='Никнейм', null=True)

    def __str__(self):
        return f'{self.surname}, {self.nic}'

    class Meta:
        verbose_name = 'Никнейм'
        verbose_name_plural = 'Никнеймы'
