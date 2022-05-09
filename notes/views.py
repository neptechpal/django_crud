from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.def 


def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()

    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    contexts = {
        'tasks': tasks,
        'form': form

    }
   
    return render(request, 'notes/index.html', contexts)

def updateTask(request, pk):
    task = Tasks.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method=="POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid:
            form.save()
        return redirect('/')
        

    context = {
        'form': form
    }
    
    return render(request,'notes/update.html', context)

def deleteTask(request, pk):
    item = Tasks.objects.get(id=pk)
    context= {
        'item': item
    }
    if request.method=='POST':
        item.delete()
        return redirect('/')
    

    return render(request, 'notes/delete.html',context)

# def register(request):
#     return render(request, 'register.html')

# def login(request):
#     return render(request, 'login.html')
# def loggedout(request):
#     return render(request, 'loggedout.html')

# def settings(request):
#     return render(request, 'settings.html')

# def home(request):
#     return render(request, 'home.html')