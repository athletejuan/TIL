# Telegram Chatbot Webhook 사용법

 - telegram에 메시지 입력 등 어떤 종류의 신호가 들어오면 바로 외부로 신호/정보 를 보내게 되는데 이 신호를 받는 곳을 Webhook이라고 함.
 - 이때 이 신호를 받아서 local로 연결해주는 프로그램: ngrok
 - Webhook: Flask/Django 등으로 구현

1. webhook 설정
 - set webhook

https://api.telegram.org

bot<token>/

setWebhook?

url=https://9841ca72.ngrok.io/950672616:AAGbW5GEAtljEIOa1_KUIV5zMM39x7DUwfQ/ <-- django의 특성상 마지막에 '/'를 붙여줘야함.

2. webhook 정보조회
 - getWebhookinfo

3. webhook 삭제
 - deleteWebhook