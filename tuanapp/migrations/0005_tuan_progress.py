# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0004_tuan_crt_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuan',
            name='progress',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
