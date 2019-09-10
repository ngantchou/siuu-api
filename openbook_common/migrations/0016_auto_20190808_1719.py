# Generated by Django 2.2.4 on 2019-08-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_common', '0015_auto_20190801_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='keyword_description_fr',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='keyword_description'),
        ),
        migrations.AddField(
            model_name='badge',
            name='keyword_description_it',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='keyword_description'),
        ),
        migrations.AddField(
            model_name='badge',
            name='keyword_description_pt_br',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='keyword_description'),
        ),
        migrations.AddField(
            model_name='badge',
            name='keyword_description_sv',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='keyword_description'),
        ),
        migrations.AddField(
            model_name='badge',
            name='keyword_description_tr',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='keyword_description'),
        ),
        migrations.AddField(
            model_name='emoji',
            name='keyword_fr',
            field=models.CharField(max_length=16, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emoji',
            name='keyword_it',
            field=models.CharField(max_length=16, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emoji',
            name='keyword_pt_br',
            field=models.CharField(max_length=16, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emoji',
            name='keyword_sv',
            field=models.CharField(max_length=16, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emoji',
            name='keyword_tr',
            field=models.CharField(max_length=16, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emojigroup',
            name='keyword_fr',
            field=models.CharField(max_length=32, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emojigroup',
            name='keyword_it',
            field=models.CharField(max_length=32, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emojigroup',
            name='keyword_pt_br',
            field=models.CharField(max_length=32, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emojigroup',
            name='keyword_sv',
            field=models.CharField(max_length=32, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='emojigroup',
            name='keyword_tr',
            field=models.CharField(max_length=32, null=True, verbose_name='keyword'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_fr',
            field=models.CharField(max_length=64, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_it',
            field=models.CharField(max_length=64, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_pt_br',
            field=models.CharField(max_length=64, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_sv',
            field=models.CharField(max_length=64, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='language',
            name='name_tr',
            field=models.CharField(max_length=64, null=True, verbose_name='name'),
        ),
    ]