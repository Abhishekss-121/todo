from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.addTask, name="addTask"),
    path("complete/<int:id>/", views.complete_task, name="complete_task"),
    path("undone/<int:id>/", views.mark_undone, name="mark_undone"),
    path("edit/<int:id>/", views.edit_task, name="edit_task"),
    path("delete/<int:id>/", views.delete_task, name="delete_task"),
]
