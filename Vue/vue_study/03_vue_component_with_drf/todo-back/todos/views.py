from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return HttpResponse(status=400)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)