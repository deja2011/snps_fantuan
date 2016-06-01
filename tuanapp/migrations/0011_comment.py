# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuanapp', '0010_auto_20160520_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.DateTimeField(verbose_name=b'date published')),
                ('content', models.TextField()),
                ('person', models.ForeignKey(to='tuanapp.Person')),
                ('tuan', models.ForeignKey(to='tuanapp.Tuan')),
            ],
        ),
    ]
