from django.shortcuts import render
from django.http import HttpResponse
import rest_framework
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo 


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer #defined in serializers.py
    queryset = Todo.objects.all()
