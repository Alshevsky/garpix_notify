# Generated by Django 3.2 on 2022-07-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garpix_notify", "0029_auto_20220630_1253"),
    ]

    operations = [
        migrations.AddField(
            model_name="notifyconfig",
            name="is_whatsapp_enabled",
            field=models.BooleanField(default=True, verbose_name="Разрешить отправку WhatsApp"),
        ),
        migrations.AddField(
            model_name="notifyconfig",
            name="whatsapp_account_sid",
            field=models.CharField(
                blank=True,
                default="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                max_length=255,
                verbose_name="WhatsApp Account SID",
            ),
        ),
        migrations.AddField(
            model_name="notifyconfig",
            name="whatsapp_auth_token",
            field=models.CharField(
                blank=True,
                default="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                max_length=255,
                verbose_name="WhatsApp Auth Token",
            ),
        ),
        migrations.AddField(
            model_name="notifyconfig",
            name="whatsapp_sender",
            field=models.CharField(blank=True, default="", max_length=30, verbose_name="Телефон отправителя WhatsApp"),
        ),
        migrations.AlterField(
            model_name="notify",
            name="type",
            field=models.IntegerField(
                choices=[
                    (0, "E-mail"),
                    (1, "SMS"),
                    (2, "Push"),
                    (3, "Telegram"),
                    (4, "Viber"),
                    (5, "System"),
                    (6, "Call"),
                    (7, "WhatsApp"),
                ],
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="notifytemplate",
            name="type",
            field=models.IntegerField(
                choices=[
                    (0, "E-mail"),
                    (1, "SMS"),
                    (2, "Push"),
                    (3, "Telegram"),
                    (4, "Viber"),
                    (5, "System"),
                    (6, "Call"),
                    (7, "WhatsApp"),
                ],
                verbose_name="Тип",
            ),
        ),
        migrations.AlterField(
            model_name="smtpaccount",
            name="sender",
            field=models.CharField(blank=True, default="", max_length=255, verbose_name="Отправитель"),
        ),
    ]
