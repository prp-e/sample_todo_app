from django.shortcuts import render
from rest_framework import viewsets, permissions
from .permissions import IsAssigned
from .models import TaskModel 
from django.contrib.auth.models import User 
from .serializers import UserSerializer, TaskSerializer
# Create your views here.

class TaskView(viewsets.ModelViewSet):  
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer 
    permission_classes = [IsAssigned] 

class UserView(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer 
    permission_classes = [permissions.IsAdminUser]