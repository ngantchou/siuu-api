# Generated by Django 2.2.3 on 2019-08-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_moderation', '0010_auto_20190601_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='moderationcategory',
            name='description_de',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='moderationcategory',
            name='title_de',
            field=models.CharField(max_length=64, null=True, verbose_name='title'),
        ),
    ]
