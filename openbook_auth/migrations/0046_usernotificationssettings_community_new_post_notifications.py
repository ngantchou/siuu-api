# Generated by Django 2.2.5 on 2019-11-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0045_userprofile_community_posts_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotificationssettings',
            name='community_new_post_notifications',
            field=models.BooleanField(default=True, verbose_name='community new post notifications'),
        ),
    ]