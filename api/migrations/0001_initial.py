# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_field', models.CharField(max_length=32)),
            ],
        ),
    ]
