# Generated by Django 3.2 on 2022-04-22 09:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garpix_notify", "0015_auto_20220422_0922"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notifyuserlistparticipant",
            options={
                "verbose_name": "Дополнительный участник списка рассылки",
                "verbose_name_plural": "Дополнительные участники списка рассылки",
            },
        ),
    ]
