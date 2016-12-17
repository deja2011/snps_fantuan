# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0015_auto_20161124_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuan',
            name='max_num',
            field=models.IntegerField(verbose_name=b'max participates'),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='min_num',
            field=models.IntegerField(verbose_name=b'min participates'),
        ),
    ]
