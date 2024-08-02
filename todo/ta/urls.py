from django.urls import path
from .views import hello, todo

urlpatterns = [
       path("", hello),
       path("todo/", todo)
]