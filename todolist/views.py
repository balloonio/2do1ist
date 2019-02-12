from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

from todolist.models import Todo

import datetime

# Create your views here.
def index(request):
    message = "Current Time: {}".format(datetime.datetime.now())
    return HttpResponse(message)

def todo_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('accounts/login/')
    todos = Todo.objects.filter(user_id=request.user.id)
    completed = sum( t.completed for t in todos )
    progress = (completed / len(todos)) * 100 if todos else 0
    return render(request, 'index.html', locals())

def add(request):
    todoname = request.POST.get('todoname')
    new_todo = Todo.objects.create(title=todoname, user_id=request.user.id)
    return HttpResponseRedirect('/')

def complete(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id, user_id=request.user.id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect('/')

def delete(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id, user_id=request.user.id)
    todo_item.delete()
    return HttpResponseRedirect('/')
    