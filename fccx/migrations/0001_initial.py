# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('houseid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cellid', models.BigIntegerField()),
                ('district_id', models.IntegerField()),
                ('cell_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('unit_price', models.IntegerField()),
                ('total_price', models.FloatField()),
            ],
        ),
    ]