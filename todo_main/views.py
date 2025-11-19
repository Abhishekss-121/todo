from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    # Pending tasks
    tasks = Task.objects.filter(completed=False).order_by('-created_at')

    # Completed tasks
    completed_tasks = Task.objects.filter(completed=True).order_by('-created_at')

    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })


def addTask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(task=title)
        return redirect("todo:home")
    return redirect("todo:home")


def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect("todo:home")


def mark_undone(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = False
    task.save()
    return redirect("todo:home")


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.task = request.POST.get("title")
        task.save()
        return redirect("todo:home")

    return render(request, "edit.html", {"task": task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("todo:home")
