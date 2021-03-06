# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t03', '0005_auto_20180815_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('height', models.FloatField(verbose_name='身高')),
                ('salary', models.CharField(max_length=30, verbose_name='工资')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('height', models.FloatField(verbose_name='身高')),
                ('face_score', models.IntegerField(verbose_name='颜值')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
