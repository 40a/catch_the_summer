# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 13:32
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, null=True, srid=4326),
        ),
    ]
