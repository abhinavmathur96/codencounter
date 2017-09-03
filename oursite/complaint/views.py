# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login

def index(request):
    in_progress = progress.objects.filter().order_by('-updated')
    in_progress = in_progress[:min(5,len(in_progress))]
    temp = []
    for i in range(len(in_progress)):
        in_progress[i] = complaint.objects.get(id=in_progress[i].id)
        if in_progress[i].completed==False:
            temp.append(in_progress[i])
    in_progress = temp[:]
    future = complaint.objects.filter(assign=None).order_by('posted')
    future = future[:min(5,len(future))]
    recent = complaint.objects.filter(completed=True).order_by('-posted')
    recent = recent[:min(5,len(recent))]
    counters = {}
    counters['Electrical'.encode('ascii')] = [len(complaint.objects.filter(department=1)),len(complaint.objects.filter(department=1,completed=True))]
    counters['Water'.encode('ascii')] = [len(complaint.objects.filter(department=2)),len(complaint.objects.filter(department=2,completed=True))]
    counters['Waste'.encode('ascii')] = [len(complaint.objects.filter(department=3)),len(complaint.objects.filter(department=3,completed=True))]
    return render(request,'index.html',{
        'title':'Home' ,
        'progress':in_progress,
        'future':future,
        'recent':recent,
        'count':counters})

def details(request, id):
    comp = complaint.objects.get(id=id)
    print request.method
    if request.method=="POST":
        form = addProgress(request.POST)
        print request.POST
        progress.objects.create(
				c_id=comp,
				action=request.POST['action'])
        return redirect('index')
    comp = complaint.objects.get(id=id)
    form = addProgress()
    return render(request,'details.html', {'comp':comp,'form':form, 'id':id})

def complete(request, id, dept_id):
    comp = complaint.objects.get(id=id)
    comp.completed = True
    comp.save()
    return redirect('department',id=dept_id)

def department_id(request,id):
    new = complaint.objects.filter(department=id,completed=False).order_by('-created')
    done = complaint.objects.filter(department=id,completed=True).order_by('-completed_at')
    resource = resources.objects.filter(department=id)
    return render(request,'department.html', {'title':'Department','new':new,'done':done,'resource':resource})

def new_compl(request):
    if request.method=="POST":
        print request.POST
        form_data = ComplaintForm(request.POST)
        if form_data.is_valid():
            print request.POST['solution']
            complaint.objects.create(
                title=request.POST['title'],
                department=int(request.POST['dept']),
                location=request.POST['location'],
                severity=int(request.POST['severity']),
                description=request.POST['description'],
                solution=request.POST.get('solution',False),
                )
            return redirect('thanks')
            
    form = ComplaintForm()
    return render(request,'new.html',{'form':form})
    

def dept_login(request):
    if request.method=="POST":
        form = LogIn(request.POST)
        if form.is_valid():
            cred = form.cleaned_data
            user = authenticate(username=cred['department_id'],password=cred['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('department',id=cred['department_id'])
                else:
                    return render(request,'login.html',{'wrong':False,'notActive':True,'form':form})
            else:
                return render(request,'login.html',{'wrong':True,'notActive':False,'form':form})
    else:
        form = LogIn()
        return render(request,'login.html',{'wrong':False,'notActive':False,'form':form})  

def thanks(request):
    return render(request,'thanks.html')
