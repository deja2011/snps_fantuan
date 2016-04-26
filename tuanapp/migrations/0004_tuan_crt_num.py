# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0003_auto_20160331_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuan',
            name='crt_num',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
