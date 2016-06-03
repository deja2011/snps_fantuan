# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0009_auto_20160516_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuan',
            name='min_num',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='max_num',
            field=models.IntegerField(default=3),
        ),
    ]
