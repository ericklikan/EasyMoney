# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_section_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='budget',
        ),
        migrations.AddField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.Budget'),
            preserve_default=False,
        ),
    ]
