# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloginfo', '0003_auto_20180917_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='picture',
            field=models.ImageField(default='', upload_to='static/images/', verbose_name='图片'),
        ),
    ]
