# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_great_britian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='great_britian',
            name='class_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='great_britian',
            name='description',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='great_britian',
            name='unit_name',
            field=models.CharField(max_length=100),
        ),
    ]