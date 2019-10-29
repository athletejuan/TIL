from django.shortcuts import render
from decouple import config
import requests

def index(request):
    return render(request, 'utilities/index.html')

# MAMAGO(Translate)

def mamago(request):
    return render(request, 'utilities/mamago.html')

def translated(request):
    # 1. 사용자가 입력한 번역을 하고 싶은 한국어 텍스트
    korean = request.GET.get('text')

    # 2. 네이버에 (Post) 번역 요청을 위해서 필요한 내용들
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    # 3. 요청을 보낼 url
    mamago_url = "https://openapi.naver.com/v1/papago/n2mt"

    # 4. 헤더 정보 구성
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret,
    }

    # 5. 우리가 요청할 데이터
    data = {
        "source": "ko",
        "target": "en",
        "text": korean,  # korean은  번역할 text를 의미하는데 이는 사용자한테 받았음
    }

    # 6. 네이버로 요청 보내기
    mamago_response = requests.post(
        mamago_url, headers=headers, data=data
    ).json()  # .json()을 통해 요청의 결과(json)를 dict로 변환한다.

    # 7. 응답 결과 보는건 같이하기(.get()도 가능)
    english = mamago_response['message']['result']['translatedText']

    context = {'korean': korean, 'english': english}
    return render(request, 'utilities/translated.html', context)