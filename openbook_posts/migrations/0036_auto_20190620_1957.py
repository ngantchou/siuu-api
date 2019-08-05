# Generated by Django 2.2.2 on 2019-06-20 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_common', '0013_language'),
        ('openbook_posts', '0035_auto_20190620_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_comments', to='openbook_common.Language'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='text',
            field=models.TextField(max_length=1500, verbose_name='text'),
        ),
    ]