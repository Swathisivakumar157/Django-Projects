from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    task = Task.objects.filter(complete=False).order_by('-update')
    completed = Task.objects.filter(complete=True)
    
    
    context ={
        'task':task,
        'completed':completed
        
    }
    return render(request,'home.html',context)
