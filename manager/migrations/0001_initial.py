# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 08:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_title', models.CharField(max_length=50)),
                ('budget_total', models.DecimalField(decimal_places=2, max_digits=17)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=50)),
                ('section_budget', models.DecimalField(decimal_places=2, max_digits=17)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Budget')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=17)),
                ('trans_title', models.CharField(max_length=50)),
                ('trans_description', models.CharField(max_length=250)),
                ('trans_datetime', models.DateTimeField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Section')),
            ],
        ),
    ]
