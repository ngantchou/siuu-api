# Generated by Django 2.2.5 on 2019-11-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_notifications', '0015_auto_20190812_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('PR', 'Post Reaction'), ('PC', 'Post Comment'), ('PCR', 'Post Comment Reply'), ('PCRA', 'Post Comment Reaction'), ('CR', 'Connection Request'), ('CC', 'Connection Confirmed'), ('F', 'Follow'), ('CI', 'Community Invite'), ('PUM', 'Post user mention'), ('PCUM', 'Post comment user mention'), ('CNP', 'New post in community')], max_length=5),
        ),
    ]
