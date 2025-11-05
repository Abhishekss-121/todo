from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def addTask(request):
    if request.method == 'POST':
        task_name = request.POST.get('task')
        if task_name:
            Task.objects.create(title=task_name)
    return redirect('home')

