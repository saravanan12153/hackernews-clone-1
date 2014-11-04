# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='points',
            new_name='upvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='downvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='scores',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
