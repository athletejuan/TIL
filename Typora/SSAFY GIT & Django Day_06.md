git ignore 하기 전에 git add를 해버린 경우

[.gitignore에 무시할 내용 입력] 후

#### unstage

파일 단위로 내리기: git rm --cached <file name>

파일 전체 내리기: git rm --cached .

--> 폴더가 존재하는 경우: git rm --cached '-r' .



끝말잇기2

mkdir wordchain

code .

README.md

# Github Flow

Fork & Pull Request



## 끝말잇기

- 이름:

저장 후 add commit push

팀원이 팀장 repository에서 fork하여  파일 수정한 후

New pull request



- 협업에 의해 변경된 버전

- 내가 수정한 버전

[원본이 있는 git 주소]



기본 방법(안전)

1. 포크를 새로 뜬다.

응용 방법

1. git remote add upstream [원본 git 주소]
2. git fetch upstream
3. git merge upstream/master --> conflict 발생

   :  Merge해줘야 함



### Collaboration

1. Push & Pull

- 동기적처리를 해야하는 업무
- 동시적 작업이 되지않음

2. Branching & Pull

- 현실 협업 모델
- 팀원들간에 동시적인 작업 가능

3. Fork & Pull Request

- Open source, Code contribution



master에서 작업해야함.

git checkout master

git pull origin master

