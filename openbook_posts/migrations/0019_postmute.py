# Generated by Django 2.2b1 on 2019-03-06 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_posts', '0018_auto_20190305_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostMute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_mutes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutes', to='openbook_posts.Post')),
            ],
            options={
                'unique_together': {('post', 'muter')},
            },
        ),
    ]
