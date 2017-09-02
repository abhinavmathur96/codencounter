# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class resources(models.Model):
    name = models.CharField(max_length=40)
    department = models.CharField(max_length=20)
    working = models.BooleanField()


class complaint(models.Model):
    loc_choices = (
        ('23','SECTOR 23'),
        ('22','SECTOR 22'),
        ('14','SECTOR 14'),
    )
    title = models.CharField(max_length = 140,default="")
    department = models.IntegerField(default=None)
    location = models.CharField(max_length=5, choices = loc_choices)
    severity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(null=True)
    solution = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add = True)
    assign = models.ForeignKey(resources, related_name = 'using', default = None, null=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now = True)

class progress(models.Model):
    id = models.OneToOneField(complaint,related_name="progress",primary_key = True)
    action = models.TextField()
    completed = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True)

    
