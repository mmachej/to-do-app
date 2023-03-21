from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('add_task', views.addTask, name="add_task"),
    path('update_task/<int:pk>/', views.updateTask, name="update_task"),
    path('delete_task/<int:pk>/', views.deleteTask, name="delete"),
    path('complete_task/<int:pk>/', views.completeTask, name="complete_task")
]