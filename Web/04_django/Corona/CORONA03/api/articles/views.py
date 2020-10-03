from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        # print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_article(request):
    # print(dir(request.data)) 
    # print(type(request.data)) dict
    # print(request.data) DRF Form으로 테스트
    # 1. Serializing 
    serializer = ArticleSerializer(data=request.data)

    # 2. .save()전에 is_valid
    # 2. 유효성 검사 & DB 저장
    # raise_exception=True 인자가 없으면 따로 예외처리
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializers = ArticleSerializer(article)
        return Response(serializers.data)
    elif request.method == 'PUT':
        # serializer = ArticleSerializer(instance=article, data=request.data)
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        article.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # serializer = ArticleSerializer(instance=article, data=request.data)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 201과 204로 나눠서 응답하는 것이 올바르지만 이번에는 요청이 정상적으로 처리된 경우만 가정하여 200으로 응답(기본값)
        return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article) # article=article_pk는 오류 발생
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)


def article_list_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/article_list_html.html', context)


def article_list_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append({
            'article_id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    
    # return render(article_json) -> template name error
    # return JsonResponse(articles_json, safe=False)
    return HttpResponse(articles_json)


def article_list_json_2(request):
    articles = Article.objects.all()
    # serializers 모듈 내부의 serialize 함수
    serialized_data = serializers.serialize('json', articles)
    # print(serialized_data)

    # content_type 설정 안하면? text/html
    return HttpResponse(serialized_data, content_type='application/json')


@api_view(['GET'])
def article_list_json_3(request):
    # 직렬화 할 데이터 DB에서 가져오기
    articles = Article.objects.all()
    serializers = ArticleSerializer(articles, many=True)

    # rest_framework 의 serializer를 리턴하려면 rest_framework.response.Response
    return Response(serializers.data)