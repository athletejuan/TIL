from django.shortcuts import render, get_object_or_404
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer


@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        # serializers.py에서 import한 Serializer의 첫번째 인자를 키워드 없이 입력하면 인스턴스로 처리되어 유효성 검사를 통과하지 못한다.
        # 인스턴스 없이 데이터만을 인자로 넣고자 할때는 data 키워드와 함께 사용해야 한다.
        # 인스턴스가 들어가는 경우에는 data 키워드 없이도 사용가능하다.
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        article.delete()
        return Response({ 'id':article_pk }, status=status.HTTP_204_NO_CONTENT)