# SSAFY Day 19 - Django_02

# Second Django

## Start app

- app의 이름이 다르더라도 django는 자체적으로 templates를 합쳐서 관리함
- 순서는 settings.py에 저장된 순서에 따라 우선권을 가짐
- SO. templates 아래에 app이름으로 하위폴더 만들고 그 안에 template 저장하여 사용

form action="/utils/output/" method="GET" <= G.E.T 전부 대문자

 html 파일 내부에서 label for="word" /

 input id="word" 서로 일치

 html 파일의 input name="user-input" /

 views.py 파일에서 get/post 요청하는 이름 request.GET.get('user-input') 서로 일치

- {% extends 'utils/base.html' %}
  - base.html으로부터 다른 html 파일로 터널을 연결
- {% block title %} {% endblock %}
  - title 정보를 연결
- {% block body %} {% endblock &}
  - body 정보를 연결