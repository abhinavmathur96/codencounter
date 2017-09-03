# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

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
    solution = models.TextField(null=True,blank=True)
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    assign = models.ForeignKey(resources, related_name = 'using', default = None, null=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now = True)

class progress(models.Model):
    c_id = models.ForeignKey(complaint,related_name="progress",default=None)
    action = models.TextField()
    updated = models.DateTimeField(default=timezone.now)

    
