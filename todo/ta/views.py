from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def hello(request):
    return render(request, "index.html")

def todo(request):
    works=TodoItem.objects.all()
    return render(request, "todo.html", {"todos":works})