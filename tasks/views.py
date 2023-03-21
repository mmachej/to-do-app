from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all().filter(complete=False).order_by('deadline')
    completed_tasks = Task.objects.all().filter(complete=True)
    form = CompleteForm()

    if request.method == "POST":
        form = CompleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    '''
    form = DeadlineForm()
    forms = []
    for task in tasks:
        form = DeadlineForm(instance=task)
        forms.append(form)

        if request.method == "POST":
            form = DeadlineForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("/")
    '''

    context = {'form.': form,
               'tasks': tasks,
               'completed_tasks': completed_tasks}

    return render(request, 'tasks/list.html', context)


def addTask(request):
    form = NewTaskForm()
    context = {'form': form}

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'tasks/add_task.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = UpdateTaskForm(instance=task)
    context = {'form': form}

    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'tasks/update_task.html', context)

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CompleteForm(instance=task)
    context = {'form': form}

    if request.method == "POST":
        form = CompleteForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'tasks/complete_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    context = {'item': item}

    return render(request, 'tasks/delete.html', context)