from .models import Task
from rest_framework import serializers
from django.contrib.auth.models import User

class TaskSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=255)
    description = serializers.TextField()
    status = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())