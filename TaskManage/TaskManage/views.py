from django.shortcuts import render, redirect
from task.models import Task
def home(request):
    task = Task.objects.all()
    return  render(request, 'home.html', {'task': task})