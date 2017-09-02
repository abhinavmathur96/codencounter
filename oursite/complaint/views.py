# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
<<<<<<< HEAD
from .forms import *
=======

DEPT_CHOICES = {
        '1':'ELECTRICAL',
        '2': 'WATER',
        '3': 'WASTE'
}
LOC_CHOICES = {
	'23': 'SECTOR 23',
	'22': 'SECTOR 22',
	'14': 'SECTOR 14'
}
>>>>>>> master

def index(request):
    in_progress = progress.objects.filter(completed=False).order_by('-updated')
    in_progress = in_progress[:min(5,len(in_progress))]
    for i in range(len(in_progress)):
        in_progress[i] = complaint.objects.get(id=in_progress[i].id)
    future = complaint.objects.filter(assign=None).order_by('created')
    future = future[:min(5,len(future))]
    recent = complaint.objects.filter(completed=True).order_by('-created')
    recent = recent[:min(5,len(recent))]
    return render(request,'index.html',{'title':'Home' ,'progress':in_progress,'future':future,'recent':recent})

def details(request, id):
    comp = complaint.objects.get(id=id)
    return render(request,'details.html',{'comp':comp})

def department(request,id):
    new = complaint.objects.filter(id in departments,completed=False).order_by('-created')
    done = complaint.objects.filter(id in departments,completed=True).order_by('-completed_at')
    resource = resources.objects.filter(department=id)
    return render(request,'department.html',{'new':new,'done':done,'resource':resource})

def new_compl(request):
    form = ComplaintForm()
    return render(request,'new.html',{'form':form})
    
    
