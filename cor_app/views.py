
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.views import View
from django.http import HttpResponse
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def addTask(request:Request):
    data = request.data
    d = User.objects.filter(username = request.user)
    u = User.objects.get(username=request.user)
    Task.objects.create(user = u, task = data['task'], description = data['description'])
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def getStudent(request: Request, id):
    # Check if student exists
    try:
        tasks = Task.objects.get(id=id)
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response({'result': 'task not found'})