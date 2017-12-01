# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 20:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0009_auto_20171126_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 20, 57, 7, 473434, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 20, 57, 7, 473413, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='couple',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 20, 57, 7, 470346, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='couple',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 20, 57, 7, 470321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 20, 57, 7, 471267, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 20, 57, 7, 471245, tzinfo=utc)),
        ),
    ]