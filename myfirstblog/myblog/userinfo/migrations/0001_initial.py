# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=20, verbose_name='收藏作者姓名')),
            ],
            options={
                'verbose_name': '作者姓名',
                'verbose_name_plural': '作者姓名',
                'db_table': 'save',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upassword', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '姓名',
                'verbose_name_plural': '姓名',
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='save',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.Userinfo'),
        ),
    ]