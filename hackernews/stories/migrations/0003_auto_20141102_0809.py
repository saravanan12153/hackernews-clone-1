# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_att',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_att',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
