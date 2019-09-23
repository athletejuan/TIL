# Advanced GIT Day_01



1. 코드 관리도구

2. 코드 (원격)저장소

   (Google Drice, DropBox)

3. 코드 협업도구

4. 개발자 이력서

### GIT remind

git bash : 윈도우 cmd 의 활용

git init (GIT 시작)

cat config (파일 내용 보기)



GIT

SCM (source code management tool)

VCS (version control system)



working directory(작업폴더)  -- > Staging Area  -- >

​											add					commit



git commit

please tell me who you are



git config --global user.email 

git config --global user.name

vi 창으로 넘어가므로: git commit -m ""



## GIT이 버젼관리를 할 수 있는 이유

### hash 기능(sha256): 암호화



git checkout: git안에서 관리되는 버젼들을 확인(just 보기만)

git log --oneline 에 보이는 log 앞자리 

git checkout [log 앞자리 입력]



git reset --hard HEAD

HEAD is now at



(처음으로) 원격저장소에서 집컴에 코드 받아올때

git clone [주소]



Sublime text



## github flow

user 1 , user 2

user 1 이 만든 repository에 user 2 가 folk

user 2 가 수정 후 add, commit, push

new pull request(메시지 전달)

user 1 이 pull request 보고 수정사항 판단, 코드 반영 (merge pull request)



github 배포 시

repository name: [본인 아이디].github.io



bootstrap template

start bootstrap