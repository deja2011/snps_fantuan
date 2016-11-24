# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0012_auto_20161124_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuan',
            old_name='date',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='tuan',
            name='crt_num',
        ),
        migrations.RemoveField(
            model_name='tuan',
            name='init',
        ),
        migrations.RemoveField(
            model_name='tuan',
            name='progress',
        ),
        migrations.AddField(
            model_name='tuan',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tuan',
            name='current_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tuan',
            name='initiator',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='max_num',
            field=models.IntegerField(verbose_name=b'min participates'),
        ),
        migrations.AlterField(
            model_name='tuan',
            name='min_num',
            field=models.IntegerField(verbose_name=b'max participates'),
        ),
    ]
