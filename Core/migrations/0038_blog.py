# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-25 12:17
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0037_auto_20170728_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
