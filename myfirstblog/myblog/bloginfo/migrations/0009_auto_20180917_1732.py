# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 09:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloginfo', '0008_auto_20180917_1728'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categorys',
        ),
    ]
