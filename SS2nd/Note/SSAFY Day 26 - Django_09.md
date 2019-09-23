### 댓글 개수

count: query_set을 보내는 방법이라 비효율

length: 효율적임



### Image Upload

views.py 의 부하를 줄여주기 위해

models.py에 meta class 를 정의함



pip install Pillow



form ... enctype = "multipart/form-data"

- application/x-www-form-urlencoded(기본값): 전부 인코딩
- text/plain: 텍스트만(인코딩x)



def create

​	article.image = request.FILES.get('image')



detail.html

<img src="{{ article.image }}" alt="">



1. 이미지가 저장되는 위치를 지정해줘야 함.
2. 정해진 위치를 DB에 저장



#### settings.py 마지막 줄에 추가

1. 실제 파일 저장소의 경로를 지정
   - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

2. 업로드된 파일의 주소(URL을 만들어줌), default: ''(root)
   - MEDIA_URL = '/media/' 



.gitignore에 media 포함되어 있어서 git에 무시됨

: (사이즈가 크고 무거운 경우가 많아) local에만 위치



#### 메인 urls.py

from django.conf.urls.static import static

from django.conf import settings



urlpatterns =[

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

or

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#### 이미지 없이 글 등록하고 싶으면

​    {% if article.image %}

      <img src="{{ article.image.url }}" alt="{{ article.image }}">

​    {% else %}

      <img src="/media/nophoto-available.png" alt="no_image">

​    {% endif %}



### Static

base.html

{% load static %}



#### favicon

favicon generator 검색하여 favicon 생성 후

하단의 링크를 base.html에 c+v

- settings.py
  - STATIC_URL = '/static/'
  - STATICFILES_DIRS=[os.path.join(BASE_DIR, 'board', 'assets')]



board > assets(folder 생성) > images(folder 생성) 로 favicon.png 파일 이동



#### 번역 안된 페이지 발견시

github django 검색.

django-docs-translations

Transifex

opensource contributor로 기여할 수 있다.