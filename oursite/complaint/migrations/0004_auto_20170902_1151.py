# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_auto_20170902_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='assign',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='using', to='complaint.resources'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='title',
            field=models.CharField(default='', max_length=140),
        ),
    ]
