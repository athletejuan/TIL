# SSAFY Day 15 Web Day 2

## Intro to CSS



* HTML은 뼈대
* CSS는 외관
* 두 개는 서로 다른 언어



html css 연동

html 파일

head 안에

link hred="(...).css" 해야 연결



파일의 용량을 줄이기 위해(공백없앤 코드)

- uglify



### CSS 사용 방법

* Inline Styling
  * tag안에 style
* Embedding
* link file(외부참조) -- 주 사용 방법



프로퍼티 값의 단위

값(Value)

1. 키워드
2. 크기단위
3. 색깔



#### Box Model

margin-top, right, bottom, left 순서

margin n px: 사방 마진 한번에



div {

margin: 20px;

padding: 5px;

border-width: ..;

border-style: ..;

border-color: ..;

border: (width, style, color) 한번에 쓰기도

}



### ** display **

#### 1. block

기본적으로 너비의 100%!

너비가 정해지면 나머지를 margin으로

##### block 레벨 요소 안에는 inline 요소를 포함할 수 있다.



display: inline는 공간적 요소 배정이 불가. (height, width 노란 underline 생김)

- block 레벨 요소 예

  : inline을 제외한 거의 모든 요소



#### 2. inline

line-height: content의 높이를 설정해줌.

inline 레벨 요소 예

(span, a, strong, img, br, input, select, textarea, button)

###### 주요 요소

- span
- input
- select
- img



##### 상세하게 설명해주는 범주의 설정이 우선

- div 보다 class 보다 id 보다 inline



#### 3. inline-block

- inline 레벨 요소처럼 한줄에 표현되지만 block처럼 height, width, margin 등을 설정 가능

  #inline-block + tab



#### 4. None

- 해당 요소를 화면에 표시하지 않는다 (공간 조차 사라짐)



### ** visible **

#### 1. visibility

##### 	: hidden

- 공간은 유지하되 컨텐츠만 사라짐



### ** Position **

#### 1. static

- 기본위치

#### 2. relative

- 자신의 위치를 기준으로 이동

#### 3. absolute

- 브라우져 화면을 기준으로 절대적인 위치

#### 4. fixed

- ex) navigation bar



python 가상환경 만들기 (python 3.7.4 --> 3.5.3)

gitbash 에서

mkdir ~/python-virtualenv

python -m venv ~/python-virtualenv/3.7.4

cd codes

mkdir django

cd django

source ~/python-virtualenv/3.7.4/Scripts/activate

exit: deactivate



cd ~

code .

.bashrc

(alias venv='source ~/python-virtualenv/3.7.4/Scripts/activate')

source ~/.bashrc

venv