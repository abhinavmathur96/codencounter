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

class progress(models.Model):
    id = models.OneToOneField(complaint,related_name="progress",primary_key = True)
    action = models.TextField()
    completed = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True)

class resources(models.Model):
    name = models.CharField(max_length=40)
    department = models.CharField(max_length=20)
    working = models.BooleanField()
    
