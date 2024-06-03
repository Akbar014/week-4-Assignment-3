from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def task (request):
    if request.method == 'POST' :
        print("ok")
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect ('home')

    task_form  = forms.TaskForm
    return render (request, 'task.html', {'forms': task_form})

def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST' :
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect ('home')
        
    return render (request, 'task.html' , {'forms' : task_form})



def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect ('home')
    