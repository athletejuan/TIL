1. 코드 관리

- SCM(Source Code Manage), VCS(Version Control System)

2. 원격 저장소

- Github, Gitlab, Bitbucket

3. 협업 도구

- Push & Pull, Fork & PR, Branch & PR
  - contributor로 등록되지 않은 상태에서 협업(Fork & PR)
  - 팀장&팀원 의 협업(Branch & PR)



### webhook

telegram에 메시지 입력 등 어떤 종류의 신호가 들어오면 바로 외부로 신호/정보 를 보내게 되는데 이 신호를 받는 곳을 Webhook이라고 함.

이때 이 신호를 받아서 local로 연결해주는 프로그램: ngrok

Webhook: Flask/Django 등으로 구현



1. webhook 설정

  --> set webhook

https://api.telegram.org

bot<token>/

setWebhook?

url=https://9841ca72.ngrok.io/950672616:AAGbW5GEAtljEIOa1_KUIV5zMM39x7DUwfQ/ <-- django의 특성상 마지막에 '/'를 붙여줘야함.



2. webhook 정보조회

  --> getWebhookinfo

3. webhook 삭제

  --> deleteWebhook



**WUNDERLIST**

**wunderlist** 

**url.py**

from decouple import config

from todos import views

token = config('TOKEN')

urlpatterns = [

..

path(f'{token}/', views.telegram)

]



**views.py**

from django.shortcut import render, redirect, get_object_or_404, *HttpResponse*

from django.views.decorator.csrf import csrf_exempt



@csrf_exempt

def telegram(request):

​	text = res.get('message').get('text')

​	chat_id = res.get('message').get('chat').get('id')

​	

​	print(request.method)

​	print(request.body)

​	return HttpResponse('any message')



**settings.py**

Allowed Host = ['9841ca72.ngrok.io'] <-- cmd창에 ngrok http 8000 입력하면 나옴.