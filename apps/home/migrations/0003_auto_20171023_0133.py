# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171020_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='index',
            field=models.IntegerField(default=100, verbose_name='教师排序'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='轮播顺序'),
        ),
    ]
