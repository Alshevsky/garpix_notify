# Generated by Django 3.2 on 2022-07-26 08:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garpix_notify", "0031_systemnotify_systemnotifyerrorlog"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="systemnotify",
            name="confirmation_needed",
        ),
        migrations.RemoveField(
            model_name="systemnotify",
            name="confirmed",
        ),
    ]
