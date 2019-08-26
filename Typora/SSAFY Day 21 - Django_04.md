# SSAFY Day 21 - Django_04

## Board

- django-admin startproject mtv_project

- - rename 04_MTV_PROJECT

- cd 04_MTV_PROJECT

- django-admin startapp board

  

  - settings.py

  ​    -	installed_apps에 'django_extensions' 추가

  ​	-	installed_apps에 'students(app name)' 추가

  

  - urls.py
    - import path, include
    - urlpatterns에 path('board/', include('board.urls')), 추가



- board>urls.py
   -	from django.urls import path
     	-	urlpatterns = []



### Board Page

1.  목록
2.  입력
3.  상세보기
4.  수정



- models.py
  - class Article(models.Model):

    - title = models.CharField(max_length=10)

      content = models.TextField(),

      created = models.DateTimeField(auto_now_add=True),

      modified = models.DateTimeField(auto_now=True)

    - def __str__(self):

      ​        return f'{self.id}: {self.title}'

---> Ctrl+s 꼭