# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_auto_20160811_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='dj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.Deejay', verbose_name='DJ'),
        ),
    ]
