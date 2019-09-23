자리이동시 현재 자리 초기화

git credential

protocol=https

host=github.com



git config --list

git config --unset --global user.name



git 협업 시 불편사항

1. 동시작업 불가

2. master branch 보호 안됨

   --> branch



## GIT Branch

### GIT 기초

 \- git init -master

 \- git add

 \- git commit

 \- git log



### GIT 원격저장소

 \- git remote add: git remote add [저장소이름] [저장소주소]

 \- git remote: 원격저장소의 리스트(이름)

 \- git remote -v: 원격저장소 목록보기



### GIT branch

- git checkout [저장소코드]: 저장소코드 상태로 돌아가서 상태.만. 확인

- git checkout master: 최신상태로 전환

- git branch: branch 목록보기

- git branch [브랜치이름]: 브랜치 생성

- git checkout -b [브랜치이름] & git switch -c [브랜치이름]: Branch 생성 후 해당 branch로 이동

- git checkout [브랜치이름]: 브랜치 변경

  --> git switch [브랜치이름]: git version update후 변경됨

- git checkout -d [브랜치이름]: Branch 삭제

- git merge [브랜치이름]: '현재 브랜치'에서 특정 브랜치를 병합



#### 1. Fast-forward merge: master에서 시작된 branch가 하나인 경우(master와 branch의 구분이 모호한 상황(?))



#### 2. auto-merge: master와 branch에서 수정한 파일이 서로 다른 경우



#### 3. merge with conflict:

Conflict 해결방법

Conflict 발생조건

 \- 동일 파일

 \- 동일 라인의 내용이 다른 경우