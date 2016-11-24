# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuan',
            name='date',
            field=models.CharField(max_length=10, verbose_name=b'date of creation'),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='init',
            field=models.CharField(max_length=30, verbose_name=b'initiator'),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='max_num',
            field=models.IntegerField(default=3, verbose_name=b'min participates'),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='min_num',
            field=models.IntegerField(default=1, verbose_name=b'max participates'),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='rest_name',
            field=models.CharField(max_length=50, verbose_name=b'restaurant name'),
        ),
    ]
