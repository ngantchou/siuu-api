# Generated by Django 2.2.5 on 2019-10-13 09:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_communities', '0028_auto_20190606_0944'),
        ('openbook_posts', '0064_auto_20191001_1853'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='toppostcommunityexclusion',
            unique_together={('user', 'community')},
        ),
    ]
