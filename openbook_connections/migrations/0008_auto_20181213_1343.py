# Generated by Django 2.1.3 on 2018-12-13 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_connections', '0007_populate_target_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targeted_connections', to=settings.AUTH_USER_MODEL),
        ),
    ]
