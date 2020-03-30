from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def home(request):
    #Fetching data from datatabase
    data = todo.objects.all()
    #Returning the data to html page
    return render(request, 'home.html', {'data': data})

def add(request):
    #fetch data from text field
    new_task = request.POST['text-input']
    #creating object of todo
    new_todo = todo(task=new_task)
    #saving it
    new_todo.save()
    #redirecting to home page
    return redirect(home)

def delete(request, todo_id):
    #getting element by id
    delete_todo = todo.objects.get(id=todo_id)
    #deleting the todo
    delete_todo.delete()
    #redirecting to home page
    return redirect(home)
