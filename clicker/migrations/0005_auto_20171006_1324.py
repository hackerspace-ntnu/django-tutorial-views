# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0004_auto_20171006_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clicker',
            name='name',
            field=models.CharField(default='Clicker', max_length=50, primary_key=True, serialize=False),
        ),
    ]