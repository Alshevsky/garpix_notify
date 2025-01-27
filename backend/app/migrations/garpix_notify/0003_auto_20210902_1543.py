# Generated by Django 3.1 on 2021-09-02 15:43

from django.db import migrations, models
import garpix_notify.mixins.user_notify_mixin


class Migration(migrations.Migration):
    dependencies = [
        ("garpix_notify", "0002_auto_20210628_0745"),
    ]

    operations = [
        migrations.AddField(
            model_name="notify",
            name="telegram_secret",
            field=models.CharField(
                default=garpix_notify.mixins.user_notify_mixin.generate_uuid,
                max_length=150,
                unique=True,
                verbose_name="Ключ подключения Telegram",
            ),
        ),
        migrations.AddField(
            model_name="notifyconfig",
            name="telegram_bot_name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Например, MySuperBot",
                max_length=255,
                verbose_name="Telegram Имя бота",
            ),
        ),
        migrations.AddField(
            model_name="notifytemplate",
            name="telegram_secret",
            field=models.CharField(
                default=garpix_notify.mixins.user_notify_mixin.generate_uuid,
                max_length=150,
                unique=True,
                verbose_name="Ключ подключения Telegram",
            ),
        ),
        migrations.AddField(
            model_name="notifyuserlistparticipant",
            name="telegram_secret",
            field=models.CharField(
                default=garpix_notify.mixins.user_notify_mixin.generate_uuid,
                max_length=150,
                unique=True,
                verbose_name="Ключ подключения Telegram",
            ),
        ),
    ]
