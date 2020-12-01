from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import TaskModel 

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskModel 
        fields = "__all__" 

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = (
            "id", 
            "username", 
            "is_staff"
        )