# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-07-30 13:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0058_auto_20200730_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='other_handles',
            field=models.CharField(default=datetime.date(2020, 7, 30), max_length=500),
            preserve_default=False,
        ),
    ]
