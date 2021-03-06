# Generated by Django 2.2 on 2019-05-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_notifications', '0007_auto_20190414_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('PR', 'Post Reaction'), ('PC', 'Post Comment'), ('PCR', 'Post Comment Reply'), ('CR', 'Connection Request'), ('CC', 'Connection Confirmed'), ('F', 'Follow'), ('CI', 'Community Invite')], max_length=5),
        ),
    ]
