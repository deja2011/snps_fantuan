# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0016_auto_20161217_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuan',
            name='start_time',
            field=models.DateTimeField(verbose_name=b'start time'),
        ),
    ]
