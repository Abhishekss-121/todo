from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    pending_tasks = Task.objects.filter(completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(completed=True).order_by('-created_at')

    if request.method == "POST":
        task_name = request.POST.get("task")
        if task_name.strip():
            Task.objects.create(task=task_name)
        return redirect("todo:home")

    return render(request, "todo/home.html", {
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks
    })


def addTask(request):
    if request.method == "POST":
        task_name = request.POST.get("task")
        Task.objects.create(task=task_name)
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
        new_title = request.POST.get("title")
        task.task = new_title
        task.save()
        return redirect("todo:home")

    return render(request, "todo/edit.html", {"task": task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("todo:home")
