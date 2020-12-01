from django.shortcuts import render
from rest_framework import viewsets, permissions 
from .models import TaskModel 
from django.contrib.auth.models import User 
from .serializers import UserSerializer, TaskSerializer
# Create your views here.

class TaskView(viewsets.ModelViewSet): 
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer 
    permission_classes = [permissions.IsAuthenticated] 

class UserView(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAdminUser]