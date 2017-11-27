# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 11:35
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('cookbook', '0008_auto_20171123_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('date_published', models.DateTimeField(default=datetime.datetime(2017, 11, 26, 11, 35, 7, 266891, tzinfo=utc))),
                ('date_last_updated', models.DateTimeField(default=datetime.datetime(2017, 11, 26, 11, 35, 7, 266915, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
        migrations.CreateModel(
            name='InCouple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couple', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Couple')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Account')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 11, 35, 7, 269984, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 11, 35, 7, 269964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='description',
            name='order',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 11, 35, 7, 267782, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 11, 35, 7, 267761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='hands_on_time',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeimage',
            name='picture',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterUniqueTogether(
            name='description',
            unique_together=set([('order', 'recipe')]),
        ),
        migrations.AlterUniqueTogether(
            name='recipeimage',
            unique_together=set([('picture', 'recipe')]),
        ),
        migrations.AddField(
            model_name='vote',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe'),
        ),
        migrations.AddField(
            model_name='couple',
            name='ingredients',
            field=models.ManyToManyField(through='cookbook.InCouple', to='cookbook.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='couple',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cookbook.Couple', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('author', 'recipe')]),
        ),
        migrations.AlterUniqueTogether(
            name='incouple',
            unique_together=set([('couple', 'ingredient')]),
        ),
    ]