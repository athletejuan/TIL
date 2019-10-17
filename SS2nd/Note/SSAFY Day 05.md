# SSAFY Day 05

## Today 목표: Telegram API

### webhook - 메시지 알림

webhook : reverse API


### webhook - url

https://api.telegram.org/bot{token}/setWebhook?url=https://<...>.ngrok.io/{token}

#### deleteWebhook

* Conflict: can't use getUpdates method while webhook is active; use deleteWebhook to delete the webhook first
  * f'{base}/{token}/deleteWebhook'


### ngrok

https://<...>.ngrok.io

### Webhook

- **Webhook** 이라는 것은 웹 서비스를 제공해주는 서버 측에서 어떠한 이벤트(또는 데이터)를 외부에 전달하는 방법 중 하나

- 우선 **Hooking**의 의미를 알아야하는데 **어떠한 액션 앞 또는 뒤에 추가로 어떠한 일을 하도록 하는 것**을 말한다. Webhook 이라는 건 웹에서 이러한 Hooking 을 할 수 있도록 제공하는 것이다. 어떠한 서비스에 대해서 Hooking을 할 수 있도록 기능을 제공해야하는데, Hooking을 해서 처리하려는 웹서버를 통해 액션을 만들고 이 액션의 URL을 등록하는 방식이 Webhook!

- 웹서비스를 제공해주는 **서버 측(LINE)**에서 **메시지가 왔을 때(어떠한 이벤트)** **해당 메시지에 대한 응답이라는 Hooking**을 만들고 싶었고 나는 Django를 통해 웹서버를 구축한 것이다. 나는 웹서버를 구축해서 Hooking 을 제공하려 했고, LINE Message API 의 설정에서 WebhookURL을 적는다는 것은 서비스를 LINE 서버 측에서 내가 만든 bot에 메시지가 왔을 때 해당 이벤트를 외부인 나의 서버로 정보를 제공할 수 있게 한 것이다.

- LINE Message API는 Hooking이 가능한 서비스를 만든거고 나는 HookingURL을 제공하는 서비스를 만든 것이당!