# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171023_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['index'], 'verbose_name': '教师', 'verbose_name_plural': '教师'},
        ),
        migrations.RemoveField(
            model_name='banner',
            name='url',
        ),
    ]
