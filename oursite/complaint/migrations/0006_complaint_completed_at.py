# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_complaint_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='completed_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
