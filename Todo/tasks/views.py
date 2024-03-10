from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks=Task.objects.all()
    form=TaskForm()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    task_context={'tasks':tasks,'form':form}
    return render(request,"task/task.html",task_context)

def update_task(request,Id):
    task=Task.objects.get(id=Id)
    form=TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request,"task/update_task.html",context)

def delete_task(request,Id):
    task=Task.objects.get(id=Id)
    context={'task':task}
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request,'task/delete.html',context)
