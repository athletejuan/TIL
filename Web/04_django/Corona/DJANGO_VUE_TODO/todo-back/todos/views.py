from django.shortcuts import render, get_object_or_404, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

@api_view(['POST'])
def todo_create(request):
    # if request.method == 'GET':
    #     todos = Todo.objects.all()
    # if request.method == 'POST':
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return HttpResponse(status=400)

@api_view(['GET','DELETE','PUT'])
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
    elif request.method == 'DELETE':
        serializer = TodoSerializer(todo)
        todo.delete()
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)
