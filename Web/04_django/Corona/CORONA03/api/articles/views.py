from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from .models import Article

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