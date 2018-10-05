# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-05-26 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentration', models.CharField(default='', max_length=140)),
                ('luminosity', models.CharField(default='', max_length=140)),
                ('next_cycle', models.CharField(default='', max_length=140)),
                ('cycle_time', models.CharField(default='', max_length=140)),
                ('plant_pump', models.CharField(default='', max_length=140)),
                ('recirculation_pump', models.CharField(default='', max_length=140)),
                ('solution_pump', models.CharField(default='', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='GardenSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentration_set', models.CharField(default='', max_length=140)),
                ('next_cycle_set', models.CharField(default='', max_length=140)),
                ('plant_pump_set', models.CharField(default='', max_length=140)),
            ],
        ),
    ]