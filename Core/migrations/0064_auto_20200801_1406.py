# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-08-01 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0063_auto_20200801_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='other_handles',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='skills',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
