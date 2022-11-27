from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class Create_task(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request:Request) -> Response:
        # getting data 
        data = request.data
        print(data)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class Get_all(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request:Request, id) -> Response:
        task = Task.objects.get(id = id)
        serializer = TaskSerializer(task)
        if task:
            return Response(serializer.data)
        return Response(serializer.errors)

class Remov_task(APIView):
    def get(self, request:Request, id) -> Response:
        task = Task.objects.get(id = id)
        task.delete()
        return Response({"delete":"OK"})
    

@api_view(['POST'])
def update_task(request:Request, id) -> Response:
    data = request.data
    task = Task.objects.get(id = id)
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

