# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_weather', '0003_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='name_en',
            field=models.CharField(default='', max_length=255),
        ),
    ]
