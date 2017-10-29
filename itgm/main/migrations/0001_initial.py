# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_n', models.IntegerField(default=0)),
                ('image', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=69)),
            ],
        ),
    ]
