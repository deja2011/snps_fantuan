# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0006_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_tuan',
            field=models.ManyToManyField(to='tuanapp.Tuan'),
        ),
        migrations.AlterField(
            model_name='person',
            name='joined_tuan',
            field=models.ManyToManyField(related_name='joind_id', to='tuanapp.Tuan'),
        ),
    ]
