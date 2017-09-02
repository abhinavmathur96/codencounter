# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0007_auto_20170902_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='assign',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='using', to='complaint.resources'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='solution',
            field=models.TextField(blank=True),
        ),
    ]