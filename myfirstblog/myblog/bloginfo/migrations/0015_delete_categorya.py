# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloginfo', '0014_remove_blog_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categorya',
        ),
    ]