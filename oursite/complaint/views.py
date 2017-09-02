# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from .forms import *

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
    return render(request,'details.html', {'comp':comp})

def department(request,id):
    new = complaint.objects.filter(id in departments,completed=False).order_by('-created')
    done = complaint.objects.filter(id in departments,completed=True).order_by('-completed_at')
    resource = resources.objects.filter(department=id)
    return render(request,'department.html',{'new':new,'done':done,'resource':resource})

def new_compl(request):
<<<<<<< HEAD
	form = ComplaintForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			print 'valid form' + str(request.POST['title'])
		else:
			print 'invalid form'
	return render(request,'new_compl.html',{'form':form})
=======
    if request.method=="POST":
        form_data = ComplaintForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            
    #form = ComplaintForm()
    return render(request,'new_compl.html',)
    
>>>>>>> f1820073fa08dd7c231c3ef96e6ebac178098358
    
def new_compl_form(request):
	print 'reached function'
	return request.POST.get('title')
