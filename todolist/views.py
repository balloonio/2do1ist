from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

from todolist.models import Todo

import datetime

# Create your views here.
def index(request):
    message = "Current Time: {}".format(datetime.datetime.now())
    return HttpResponse(message)

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', locals())

def add(request):
    todoname = request.POST.get('todoname')
    new_todo = Todo.objects.create(title=todoname)
    return HttpResponseRedirect('/')

def complete(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect('/')

def delete(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id)
    todo_item.delete()
    return HttpResponseRedirect('/')
    