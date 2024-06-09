from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index (request):
  todo = Todo.objects.all()
  return render(request, 'index.html', {'todos': todo})

def add (request):
  title = request.GET['title']
  new_todo = Todo.objects.create(title=title)
  new_todo.save()
  return redirect("/")

def delete (request, vi):
  todo = Todo.objects.get(id=vi)
  todo.delete()
  return redirect("/")
