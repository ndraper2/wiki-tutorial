# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-01 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
