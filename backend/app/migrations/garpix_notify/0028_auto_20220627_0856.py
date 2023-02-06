# Generated by Django 3.1 on 2022-06-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garpix_notify", "0027_auto_20220627_0827"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notifyconfig",
            name="telegram_parse_mode",
            field=models.CharField(
                blank=True,
                choices=[("", "Без форматирования"), ("HTML", "HTML"), ("Markdown", "Markdown")],
                default="",
                max_length=100,
                verbose_name="Тип парсера телеграм сообщений",
            ),
        ),
    ]
