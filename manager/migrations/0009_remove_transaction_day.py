# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_transaction_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='day',
        ),
    ]