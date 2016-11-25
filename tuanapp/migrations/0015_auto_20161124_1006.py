# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0014_auto_20161124_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuan',
            name='initiator',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='start_time',
            field=models.CharField(max_length=50, verbose_name=b'start time'),
        ),
    ]
