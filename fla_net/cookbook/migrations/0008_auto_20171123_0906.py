# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0007_auto_20171121_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 23, 9, 6, 33, 703385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 23, 9, 6, 33, 703363, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 23, 9, 6, 33, 701227, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 23, 9, 6, 33, 701200, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='recipeimage',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe'),
        ),
    ]
