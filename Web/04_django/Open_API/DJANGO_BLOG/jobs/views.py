from django.shortcuts import render
from .models import Job
from faker import Faker

def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')

    # DB에 이름이 있는지 확인
    person = Job.objects.filter(name=name).first()
    # person = Job.objects.get(name=name)
    # 위에 것보다 이게 더 간단하지만 .get() 은 에러메시지를 띄운다.

    # DB 에 이미 같은 name 이 있으면 기존 name 의 past_job 가져오기, (레코드가 있으면 None이 아니니까 True일 것이다.)
    if person:
        past_job = person.past_job
    # 없으면 DB 에 새로 저장한 후 가져오기
    else:
        faker = Faker('ko-KR')
        past_job = faker.job()
        person = Job(name=name, past_job=past_job)  # 새로운 레코드를 추가한다.
        person.save()
    return render(request, 'jobs/past_life.html', {'person':person})