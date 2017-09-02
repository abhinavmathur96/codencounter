# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class complaint(models.Model):
    loc_choices = (
        ('23','SECTOR 23'),
        ('22','SECTOR 22'),
        ('14','SECTOR 14'),
    )
    departments = models.CharField(max_length = 20)
    location = models.CharField(max_length=5, choices = loc_choices)
    severity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField()
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add = True)



