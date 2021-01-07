# DB Relation



## Board Template CRUD

#### Django CRUD remind

0. Projet BOARD -> app posts

1. Model Post

   - title

   - content
   - created_at
   - updated_at

2. url
   - /create
   - /1/
   - /index
   - /1/update/
   - /1/delete/
   - /1/create_comment
3. Model Comment
   - content
   - created_at
   - updated_at
   - article = models.ForeignKey(Article, on_delete=models.CASCADE)
     - CASCADE: 반(1)을 삭제시 해당 반 소속학생(N) 같이 연동삭제



#### Comment

- 관계없음 의 관계
- 1:1 관계
  - 남-여 결혼 관계, 이름-주민번호 관계
- **1:N 관계(one to many)**
  - 반-학생 관계
- M:N 관계(many to many)
  - 1:N 을 활용하여 만든다



#### db.sqlite visualize function

pip install django-extensions



**settings.py**

installed_apps

'django_extensions'



python manage.py shell_plus

Comment.objects.create(content="첫번째 댓글", article=article_2)

article_2.comment_set.last()