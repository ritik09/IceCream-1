# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-04-16 23:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0053_auto_20200417_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='github_username',
            field=models.CharField(blank=True, default='', max_length=39, null=True, validators=[django.core.validators.RegexValidator(regex='/^[a-z\\d](?:[a-z\\d]|-(?=[a-z\\d])){0,38}$/i')]),
        ),
    ]
