from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

@api_view(['POST'])
def create_task(request: Request) -> Response:
    # getting data 
    data = request.data
    print(data)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def update_task(request:Request, id) -> Response:
    data = request.data
    task = Task.objects.get(id = id)
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)