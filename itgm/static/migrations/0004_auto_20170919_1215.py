# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 10:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20170919_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
        migrations.AddField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 19, 12, 15, 32, 229178)),
        ),
    ]
