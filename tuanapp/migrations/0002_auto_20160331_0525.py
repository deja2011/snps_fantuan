# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resturant_name', models.CharField(max_length=50)),
                ('max_num', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
