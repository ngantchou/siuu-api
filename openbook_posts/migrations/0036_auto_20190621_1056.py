# Generated by Django 2.2.2 on 2019-06-21 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_common', '0012_auto_20190202_1320'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_posts', '0035_auto_20190606_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postreaction',
            name='emoji',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='openbook_common.Emoji'),
        ),
        migrations.CreateModel(
            name='PostCommentReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('emoji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_reactions', to='openbook_common.Emoji')),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='openbook_posts.PostComment')),
                ('reactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_reactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('reactor', 'post_comment')},
            },
        ),
        migrations.CreateModel(
            name='PostCommentMute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_mutes', to=settings.AUTH_USER_MODEL)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutes', to='openbook_posts.PostComment')),
            ],
            options={
                'unique_together': {('post_comment', 'muter')},
            },
        ),
    ]
