
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
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
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

@api_view(['GET'])
def deletTask(request:Request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return Response({'results':'task removed successfully'})

@api_view(['POST'])
def updateTask(request:Request, id):
    t_data = Task.objects.get(id = id)
    r_data = request.data
    data = {
        'task':r_data.get('task'),
        'description':r_data.get('description'),
        'status':r_data.get('status')
    }

    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)