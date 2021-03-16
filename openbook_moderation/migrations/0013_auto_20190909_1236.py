# Generated by Django 2.2.5 on 2019-09-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_moderation', '0012_auto_20190808_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='moderationcategory',
            name='description_da',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='moderationcategory',
            name='description_hu',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='moderationcategory',
            name='description_nl',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='moderationcategory',
            name='title_da',
            field=models.CharField(max_length=64, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='moderationcategory',
            name='title_hu',
            field=models.CharField(max_length=64, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='moderationcategory',
            name='title_nl',
            field=models.CharField(max_length=64, null=True, verbose_name='title'),
        ),
    ]
