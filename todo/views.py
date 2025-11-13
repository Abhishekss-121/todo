from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Home Page – shows tasks and handles form submission
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

    return render(request, 'todo/home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })

# Add a new task
def addTask(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(task=task_title)
    return redirect('todo:home')

# Mark a task as complete
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('todo:home')

# Edit a task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            task.task = new_title
            task.save()
            return redirect('todo:home')
    return render(request, 'todo/edit_task.html', {'task': task})

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo:home')
