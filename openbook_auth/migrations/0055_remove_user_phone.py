# Generated by Django 2.2.16 on 2021-01-08 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0054_auto_20210106_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
