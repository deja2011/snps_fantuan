# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0007_auto_20160504_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='none@synopsts.com', unique=True, max_length=254),
            preserve_default=False,
        ),
    ]
