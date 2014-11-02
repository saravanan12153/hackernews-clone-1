# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20141102_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
