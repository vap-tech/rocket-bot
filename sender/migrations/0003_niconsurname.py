# Generated by Django 5.0.6 on 2024-06-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0002_alter_botsetting_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NicOnSurname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, null=True, verbose_name='Фамилия')),
                ('nic', models.CharField(max_length=100, null=True, verbose_name='Никнейм')),
            ],
            options={
                'verbose_name': 'Никнейм',
                'verbose_name_plural': 'Никнеймы',
            },
        ),
    ]
