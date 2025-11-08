from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = True
    task.save()
    return redirect('home')

def unmark(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = False
    task.save()
    return redirect('home')

def edit(request,pk):
    get = get_object_or_404(Task , pk=pk)
    if request.method == 'POST':
        new = request.POST['task']
        get.task = new
        get.save()
        return redirect('home')
    else:
        context = {
            'get':get,
        }
        return render(request,'edit.html',context)

def dele(request,pk):
    dele = get_object_or_404(Task , pk=pk)
    dele.delete()
    return redirect('home')