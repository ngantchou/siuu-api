# Generated by Django 2.1.5 on 2019-03-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='notifications_enabled',
            field=models.BooleanField(default=True, verbose_name='notifications enabled'),
        ),
    ]
