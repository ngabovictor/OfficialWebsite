# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20170207_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='classifications',
            field=models.CharField(choices=[('Web', 'Web'), ('App', 'App'), ('Graphics', 'Graphics')], default='App', max_length=200),
        ),
    ]
