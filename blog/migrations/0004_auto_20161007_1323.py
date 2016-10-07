# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-07 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161002_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(default='Life', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='post_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
