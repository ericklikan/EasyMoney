# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_remove_transaction_trans_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='day',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]