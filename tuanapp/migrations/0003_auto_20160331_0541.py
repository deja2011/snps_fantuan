# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0002_auto_20160331_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rest_name', models.CharField(max_length=50)),
                ('max_num', models.CharField(max_length=30)),
                ('init', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Yue',
        ),
    ]
