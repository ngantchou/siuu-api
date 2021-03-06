# Generated by Django 2.2.16 on 2021-01-08 15:29

from django.db import migrations, models
import openbook_posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0071_auto_20201019_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=200, null=True, validators=[openbook_posts.validators.post_text_hashtags_validator], verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='postlink',
            name='link',
            field=models.TextField(max_length=200),
        ),
    ]
