# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-10 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('occupation', models.CharField(max_length=250)),
                ('blood_group', models.CharField(max_length=50)),
                ('date_of_birth', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]