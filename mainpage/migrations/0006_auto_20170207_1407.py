# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20170203_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='classifications',
            field=models.CharField(choices=[('App', 'App'), ('Graphics', 'Graphics'), ('Web', 'Web')], default='App', max_length=200),
        ),
    ]
