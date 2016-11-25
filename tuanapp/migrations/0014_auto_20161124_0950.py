# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0013_auto_20161124_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuan',
            name='start_time',
            field=models.CharField(max_length=10, verbose_name=b'start time'),
        ),
    ]
