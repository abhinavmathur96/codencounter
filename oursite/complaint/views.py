# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

def index(request):
    in_progress = progress.objects.filter(completed=False).order_by('-update')
    in_progress = in_progress[:min(5,len(in_progress))]
    for i in range(len(in_progress)):
        in_progress[i] = complaint.objects.get(id=in_progress[i].id).title
    future = complaint.objects.filter(assign=null)
