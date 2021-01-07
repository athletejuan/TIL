# SSAFY Day 19 - Django_02

# Second Django

<<<<<<< HEAD
=======
## Class 1.

#### template 상속

1. 공통적으로 쓸 템플릿(코드)을 뽑아낸다.
2. 해당 파일(base.html)을 따로 만들고,
3. 활용할 다른 템플릿 파일에서 불러와 쓴다.



1. 사용자의 입력을 받아
   - /artii/
2. artii API를 통해 ascii art
   - /artii/result



#### artii API code (views.py)

```
def artii(request):
    return render(request, 'artii/artii.html')

def result(request):
    # 1. 단어를 받아온다.
    word = request.GET.get('word')
    # 2. artii api를 통해 ascii art 결과들을 요청하고,
    url = 'http://artii.herokuapp.com/make?text='
    result = requests.get(url + word).text
    # 3. 결과를 받아와 보여준다.
    context = {
        'word':word,
        'result':result,
    }
    return render(request, 'artii/result.html', context)
```





1. 앱 만들기 python manage.py startapp 
2. 등록하기 settings.py installed apps



- templates 폴더를 찾고 없으면 다른 앱 안의 templates 폴더까지는 찾아보지만 상위폴더는 찾지 않는다
  - So. settings.py안의 TEMPLATES =[{ .. 'DIR':[ ] }] 수정
    --> [os.path.join(BASE_DIR, 'first_app', 'templates')]

- 즉 다른 앱 안의 templates 폴더안에 있는 template는 별다른 작업 없이도 불러와서 쓸 수 있다.





## Class 3.

>>>>>>> 5037ed108f0cdf4ee9b7d89c6f2a5aa144e5646f
## Start app

- app의 이름이 다르더라도 django는 자체적으로 templates를 합쳐서 관리함
- 순서는 settings.py에 저장된 순서에 따라 우선권을 가짐
<<<<<<< HEAD
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
=======
  
- SO. templates 아래에 app이름으로 하위폴더 만들고 그 안에 template 저장하여 사용



form action="/utils/output/" method="GET" <= G.E.T 전부 대문자

​		html 파일 내부에서 label for="word" / 

​		input id="word" 서로 일치



​		html 파일의 input name="user-input" / 

​		views.py 파일에서 get/post 요청하는 이름 request.GET.get('user-input') 서로 일치



- {% extends 'utils/base.html' %}
  - base.html으로부터 다른 html 파일로 터널을 연결

- {% block title %} {% endblock %}
  - title 정보를 연결

- {% block body %} {% endblock &}
  - body 정보를 연결



- pip install art



- ngrok download
  - 실행파일 django 폴더로 이동
  - cmd 창에서 ngrok http 8000

>>>>>>> 5037ed108f0cdf4ee9b7d89c6f2a5aa144e5646f
