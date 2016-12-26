# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=2)),
                ('iata', models.CharField(max_length=3)),
            ],
        ),
    ]