# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloginfo', '0016_auto_20180917_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='save',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
