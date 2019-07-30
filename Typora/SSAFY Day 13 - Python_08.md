# SSAFY Day 13 Python Day 8

## Git Practice



A: Team Leader / B: Team Member

### 단순협업

ReadMe(markdown)



* mkdir git_practice

* cd git_practice

* code .

vscode 에서 README.md 파일 생성



* git init (git 시작)

* ls .git (확인)

* cat .git/config (선택사항)

* git status (선택사항)



* github에 repository 생성(name은 임의로 가능)



#### git collabo repository 생성 후

* git add .
* git commit -m " ... "
* git remote add origin https://github.com/sspy21/collabo.git



git status 상에서 붉은 글씨가 떠있으면 git pull 안됨.



협업시

하나의 파일을 두 사람이 동시에 수정한 후 순차적으로 커밋(commit)하고 병합(merging)하면

먼저 커밋(commit)한 사람이 수정한 내용이 먼저, 나중에 커밋한 사람이 수정한 내용이 뒤에 붙는다.



* Checkout

과거 커밋한 순간(환경)으로 돌아가는 기능 (기본적으로는 master 환경에 위치)

git checkout ....





git branch ....



