# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-02 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170902_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='content',
            field=models.TextField(),
        ),
    ]
