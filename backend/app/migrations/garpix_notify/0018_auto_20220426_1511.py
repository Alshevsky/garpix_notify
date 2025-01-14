# Generated by Django 3.2 on 2022-04-26 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("garpix_notify", "0017_alter_notifyconfig_sms_url_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notifycategory",
            name="template_choice",
        ),
        migrations.AddField(
            model_name="notifytemplate",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="templates",
                to="garpix_notify.notifycategory",
                verbose_name="Категория",
            ),
        ),
        migrations.AddField(
            model_name="notifytemplate",
            name="email",
            field=models.EmailField(
                blank=True,
                help_text="Используется только в случае отсутствия указанного пользователя",
                max_length=255,
                null=True,
                verbose_name="Email получатель",
            ),
        ),
        migrations.AddField(
            model_name="notifytemplate",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь (получатель)",
            ),
        ),
    ]
