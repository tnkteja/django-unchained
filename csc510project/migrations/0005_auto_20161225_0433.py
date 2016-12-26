# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-25 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('csc510project', '0004_extendeduser_activationkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='primaryemail',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='resetkey',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='activationkey',
            field=models.CharField(max_length=255),
        ),
    ]