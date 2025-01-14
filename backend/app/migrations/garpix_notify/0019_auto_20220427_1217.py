# Generated by Django 3.2 on 2022-04-27 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garpix_notify", "0018_auto_20220426_1511"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notify",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifies",
                to="garpix_notify.notifycategory",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="notifytemplate",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="templates",
                to="garpix_notify.notifycategory",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="smtpaccount",
            name="host",
            field=models.CharField(default="smtp.yandex.com", max_length=255, verbose_name="Хост"),
        ),
        migrations.AlterField(
            model_name="smtpaccount",
            name="is_use_ssl",
            field=models.BooleanField(default=True, verbose_name="Использовать SSL?"),
        ),
        migrations.AlterField(
            model_name="smtpaccount",
            name="is_use_tls",
            field=models.BooleanField(default=False, verbose_name="Использовать TLS?"),
        ),
    ]
