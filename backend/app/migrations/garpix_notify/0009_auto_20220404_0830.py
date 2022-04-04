# Generated by Django 3.1 on 2022-04-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_notify', '0008_auto_20220401_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifyconfig',
            name='sms_url',
        ),
        migrations.AddField(
            model_name='notifyconfig',
            name='sms_url_type',
            field=models.IntegerField(choices=[(0, 'sms.ru'), (1, 'web.szk-info.ru')], default=0, verbose_name='URL СМС провайдера'),
        ),
    ]
