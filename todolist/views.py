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
    if 'LAST_OP' not in request.session:
        green_from, green_to = get_progress_bar_values(
            'LOGIN', completed, len(todos) )
    else:
        green_from, green_to = get_progress_bar_values(
            request.session['LAST_OP'], completed, len(todos) )
    return render(request, 'index.html', locals())

def get_progress_bar_values(last_op, todo_done, todo_total):
    if last_op == 'LOGIN':
        if todo_total == 0:
            return 0, 0
        else:
            return 0, todo_done / todo_total
    elif last_op == 'COM':
        return (todo_done-1) / todo_total, todo_done / todo_total
    elif last_op == 'ADD':
        return (0 if todo_total == 1 else (todo_done / (todo_total - 1))), todo_done / todo_total
    elif last_op == 'DEL DONE':
        return (todo_done + 1)/(todo_total+1), (0 if todo_total == 0 else (todo_done/todo_total))
    elif last_op == 'DEL TODO':
        return (todo_done)/(todo_total+1), (0 if todo_total == 0 else (todo_done/todo_total))

def add(request):
    request.session['LAST_OP'] = 'ADD'
    todoname = request.POST.get('todoname')
    new_todo = Todo.objects.create(title=todoname, user_id=request.user.id)
    return HttpResponseRedirect('/')

def complete(request, todo_id):
    request.session['LAST_OP'] = 'COM'
    todo_item = get_object_or_404(Todo, id=todo_id, user_id=request.user.id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect('/')

def delete(request, todo_id):
    todo_item = get_object_or_404(Todo, id=todo_id, user_id=request.user.id)
    if todo_item.completed:
        request.session['LAST_OP'] = 'DEL DONE'
    else:
        request.session['LAST_OP'] = 'DEL TODO'
    todo_item.delete()
    return HttpResponseRedirect('/')
    