# SSAFY Day 20 - Django_03

### Python & Django



Code

1. 테이블 생성 (Sheet, Header)

2. 데이터 조작 (Create, Read, Update, Delete)

   ​	|

중개자(Python / ORM)

​			|

D.B(SQL)



### ORM(Object Relational Mapping)

: Python의 언어를 D.B에 적용하기 위한 일종의 번역자



#### models.py 작성 후 

- python manage.py makemigrations

   --> models 파일들을 찾아봄

- python manage.py migrate



#### models.py 수정 후 makemigrations 실행시

-> 원래 있던 데이터들은 어떻게 할것인지?

 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py

1. 빈 열에 null 값을 넣고 실행
2. 실행 중단



- python manage.py shell

  article = Article()
  article.title = "first title"
  article.content = "first content"
  article.save()
  Article.objects.all()

  first_article = Article.objects.first()
  first_article
  first_article.title



- 강의시 create.html 파일 만들었다가 필요 없음을 설명.