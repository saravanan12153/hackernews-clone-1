# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20141104_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='points',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='scores',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
