# SSAFY Day 18 - Django_01

# First Django

## Start project

- 가상(독립)환경 생성 및 django 설치

  $ pwd

  ~/TIL/04_django

  $ py -m venv venv

  $ pip install django

  $ code .

- django 프로젝트 만들기 & 프로젝트 폴더 이름 바꾸기

$ source ./venv/Scripts/activate # vscode 에서 python: select interpreter로 venv 선택

(venv)

$ django-admin startproject first_project

(venv)

$ mv first_project FIRST-PROJECT

(venv)

$ cd FIRST-PROJECT

(venv)

$ ls

first_project/ manage.py

- Django 강의에서의 용어 설명

| 이름                        | 설명                                                         |
| --------------------------- | ------------------------------------------------------------ |
| 프로젝트 루트(Project ROOT) | 프로젝트 폴더의 최상단.(manage.py가 위치한 곳)               |
| 마스터 앱(Master App)       | 프로젝트 이름과 같은 이름의 폴더. 프로젝트 루트에 위치한다. 프로젝트 생성시 자동으로 생성된다.(first_app/) |
| 마스터 세팅                 | <MASTER_APP>/setting.py 파일을 의미. 프로젝트 전체의 설정을 저장하는 곳. 새로운 App을 생성하면 반드시 INSTALLED_APPS에 등록해야 한다. |
| 마스터 URL                  | <MASTER_APP>/urls.py 파일을 의미. 프로젝트 전체의 URL 포워딩을 담당한다. |

- 서버 실행해보기

  (venv)

  $ python manage.py runserver # 프로젝트 루트에서 실행해야 한다.

## First App

Django 프로젝트는 App 들의 총합이다.

- 첫 번째 App 생성하기

  (venv)

  $ django-admin startapp utils

  $ ls

  first_project/ utils/ manage.py db.sqlite3





## Django Flow

1. master URL (<MASTER_APP>/urls.py)

2. App URL (<APP_NAME>/urls.py)

3. App view (<APP_NAME>/views.py)

4. App Template(<APP_NAME>/templates/.html)

   ## Routing

   $ APP/urls.py

   from django.urls import path

   from . import views

   urlpatterns = [

   path('URL_PATTERN', views.VIEW_NAME),

   path('URL_PATTERN/int:num', view.second_view),

   path('URL_PATTERN/str:num', views.third_view),

   ]

   ## View

   $ APP/views.py

   from django.shortcuts import render

   def first_view(request):

    return render(request, 'first_template.html')

   def second_view(request, num):

    return render(request, 'second_template.html')

   def third_view(request, num):

    return render(request, 'third_template.html')

   ## Template

   {% for num in numbers %}

    {{ num }}

   {% endfor %}

   {% if word == 'apple '%} This is Apple {% else %} This is not Apple {% endif %}