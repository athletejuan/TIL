# SSAFY Day 20 - Django_03

## Model (Template View)

- Model이란 Column
  - 데이터의 범위를 필요에 따라 설정, 한정 하는 역할
  - 데이터를 수집할때 가장 중요한건 Column의 header를 설정하는 것.



- django-admin startproject model_project
  - rename 03_MODEL_PROJECT
- cd 03_MODEL_PROJECT

- django-admin startapp students



settings.py

​	-	installed_apps에 'students(app name)' 추가



- pip install ipython
  - pip install ipython[notebook]
    -  pip install django django-extensions ipython ipython[notebook] <- 한줄 설치



- models.py

  - class Student(models.Model):

    - name = models.CharField(max_length=10)

      email = models.CharField(max_length=50),

      github_id = models.CharField(max_length=50),

      age = models.IntegerField()



### Python & Django



Code

1. 테이블 생성 (Sheet, Header)

2. 데이터 조작 (Create, Read, Update, Delete)

   ​	|

중개자(Python / ORM)

​			|

D.B(SQL)



- python manage.py makemigrations
- python manage.py migrate



python manage.py shell_plus



- installed_apps 에 'django_extensions' 추가



python manage.py shell_plus --notebook



### CRUD

from students.models import Student

#### Create

student = Student()
student.name = 'Tak'
student.email = 'tak@hphk.kr'
student.github_id = 'edutak'
#student.age = 35
student.save()

 --> student = Student(name='jason', email='jason@hphk.kr', github_id='edujason').save()

 --> student = Student.objects.create(name='change', email='change@hphk.kr', github_id='educhange')



#### Read(Retrive)

s1 = Student.objects.get(id=1)
s2 = Student.objects.get(id=6)



#### Update

s1 = Student.objects.get(id=1)

s1.age = 50

s1.save()



#### Delete

s5 = Student.objects.get(id=6)

s5.delete()





### Crawling CRUD

in Django shell-plus notebook

import requests
from bs4 import BeautifulSoup

from real_data.models import HotIssue



def get_hot_issue():    
    url = 'https://datalab.naver.com/keyword/realtimeList.naver'
    headers = {'user-agent': ':)'}
    res = requests.get(url).text

    soup = BeautifulSoup(res, 'html.parser')
    
        date_sel = '#content > div > div.section_serch_area > div > div.date_indo > a.date_box._date_trigger > span.date_txt._title_ymd'
        time_sel = '#content > div > div.section_serch_area > div > div.time_indo > a.time_box._time_trigger > span.time_txt._title_hms'
        rank_sel = f'#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child({i}) > a > em'
        keyword_sel = f'#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child({i}) > a > span'
    
        date = soup.select_one(date_sel).text
        time = soup.select_one(time_sel).text
        rank = soup.select_one(rank_sel).text
        keyword = soup.select_one(keyword_sel).text


for i in range(1,21):
    HotIssue.objects.create(
        date=get_hot_issue(i).get('date'),
        time=get_hot_issue(i).get('time'),
        rank=get_hot_issue(i).get('rank'),
        keyword=get_hot_issue(i).get('keyword')
    )        