# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_auto_20170210_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='classifications',
            field=models.CharField(choices=[('App', 'App'), ('Web', 'Web'), ('Graphics', 'Graphics')], default='App', max_length=200),
        ),
    ]
