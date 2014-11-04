# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20141104_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='total_votes',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
