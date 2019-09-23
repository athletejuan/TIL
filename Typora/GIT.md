```
# Git

> Git은 분산버전관리시스템(DVCS)이다.
>
> 소스코드의 이력을 관리한다.

* 참고 문서
  * [Git scm](https://git-scm.com/book/ko/v2)
  * [Git 입문](https://backlog.com/git-tutorial/kr/)

## 1. git 설정

git 커밋을 하기 위해서는 초기에 작성자(author) 설정을 반드시 하여야 한다.

​```bash
$ git config --global user.name {사용자이름}
$ git config --global user.email {사용자이메일}
​```

현재 global로 설정된 환경설정을 확인하기 위해서는 아래의 명령어를 작성한다.

​```bash
$ git config --global --list
user.email=edutak.ssafy@gmail.com
user.name=edutak
​```



## 2. git 활용 기초

1. 로컬 git 저장소 설정

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/student/Desktop/algorithms/.git/
   (master) $
   ```

   * 해당 디렉토리에 `.git/` 폴더가 생성 된다.
   * 항상 `git init` 하기 전에는 해당 폴더가 이미 로컬 저장소인지(`(master)` 여부) 확인 하여야 한다.

2. add

   ```bash
   $ git add .
   $ git add README.md a.txt
   $ git add folder/
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 1 commit.
     (use "git push" to publish your local commits)
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   
           Git.md
   
   nothing added to commit but untracked files present (use "git add" to track)
   
   ```

   * `add` 명령어를 통해서 `Working directory`에서 `INDEX(staging area)`로 특정 파일들을 이동시킨다.
   * 커밋을 할 목록에 쌓는 것이다.

3. commit

   ```bash
   $ git commit -m '커밋메시지'
   $ git commit
   [master a1a04a7] README 제목 작성
    1 file changed, 1 insertion(+)
   $ git log
   ```

4. 커밋 히스토리 확인하기(`log`)

   ```bash
   $ git log
   $ git log -2
   $ git log --oneline
   ```

5. 현재 git 상태 알아보기(`status`) **중요! 자주 입력해서 확인하자!**

   ```bash
   $ git status
   ```

## 3. 원격저장소(remote) 활용하기

### 1. 기초

1. remote 저장소 등록

   ```bash
   $ git remote add origin {github URL}
   ```

   * 원격 저장소를 `origin` 이라는 이름으로 `URL` 을 등록한다.

2. remote 저장소 확인

   ```bash
   $ git remote -v
   ```

3. remote 저장소 삭제

   ```bash
   $ git remote rm {저장소 이름}
   ```

### 2. Push - Pull

1. 원격 저장소로 보내기 (`push`)

    ```bash
    $ git push origin master
    ```

2. 원격 저장소로부터 가져오기(`pull`)

   ```bash
   $ git pull origin master
   ```

### 3. Push-Pull 시나리오

Local A, Local B, Github으로 활용을 하는 경우 원격저장소 이력과 달라져서 충돌이 발생할 수 있다. 따라서, 항상 작업을 시작하기전에 `pull` 을 받고, 작업을 완료한 이후에 `push`를 진행하면 충돌 사항이 발생하지 않는다!

1. auto-merge

   * 동일한 파일을 수정하지 않은 경우 자동으로 merge commit이 발생 한다.

   ```
   1. Local A에서 작업 후 Push
   2. Local B에서 작업 시 pull을 받지 않음.
   3. Local B에서 다른 파일 작업 후 commit -> push
   4. 오류 발생(~~git pull~~)
   5. Local B에서 git pull
   6. 자동으로 vim commit 할 수 있도록 뜸.
   7. 저장하면, merge commit 발생
   8. Local B에서 git push!
   ```

2. merge conflict

   * 다른 이력(커밋)으로 동일한 파일이 수정되는 경우 merge conflict 발생.
   * 직접 충돌 파일을 해결 해야 한다!

   ```
   1. Local A에서 작업 후 Push
   2. Local B에서 작업 시 pull을 받지 않음.
   3. Local B에서 동일 파일 작업 후 commit -> push
   4. 오류 발생(~~git pull~~)
   5. Local B에서 git pull
   6. 충돌 발생(merge conflict)
   7. 직접 오류 수정 및 add, commit
   8. Local B에서 git push
   ```

   * `git status` 명령어를 통해 어느 파일에서 충돌이 발생하였는지 확인 가능!

   * 실제 파일 예시

     ```
     <<<<<<< HEAD
     Local B작업
     =======
     원격 저장소에 기록된 작업
     >>>>>>> fajskh213ht12h4fahjkfhsdk
     ```


## 4. 되돌리기

1. `Staging area` 에서 unstage

   ```bash
   $ git status
   On branch master
   Your branch is ahead of 'origin/master' by 1 commit.
     (use "git push" to publish your local commits)
   
   Changes to be committed:
     (use "git reset HEAD <file>..." to unstage)
   
           deleted:    b.txt
   $ git reset HEAD b.txt
   ```

2. commit 메시지 수정하기

   ```bash
   $ git commit --amend
   ```

   * 커밋 메시지를 수정하게 되면 해시값이 변경되어 이력이 변화하게 된다.

   * 따라서 원격 저장소에 push된 이력이라면 절대 변경하면 안된다!

   * 커밋을 하는 과정에서 파일을 빠뜨렸다면, 위의 명령어를 통해서 수정할 수도 있다!

     ```bash
     $ git add omit_file.txt
     $ git commit --amend
     ```

3. `working directory` 변경사항 버리기

   ```bash
   $ git checkout -- 파일명
   ```

   * 변경사항이 모두 삭제 되고, 해당 파일의 이전 커밋 상태로 변화한다!

## Branch 관리

​```bash
$ git branch {브랜치명} # 브랜치 생성
$ git checkout {브랜치명} # 브랜치 이동
$ git branch -d {브랜치명} # 브랜치 삭제
​```

​```bash
$ git checkout -b {브랜치명} # 브랜치 생성 및 이동
​```

​```bash
$ git merge {브랜치명} # 브랜치명을 지금 브랜치로 병합
(master) $ git merge feature/index # feature/index 브랜치를 master로 병합
​```

### 상황 1. fast-foward

1. feature/test branch 생성 및 이동

   ```bash
   $ git checkout -b feature/test
   Switched to a new branch 'feature/test'
   (feature/test) $
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch test.html
   $ git add .
   $ git commit -m 'Complete test.html'
   ```

3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   (master) $
   ```

4. master에 병합

   ```bash
   $ git merge feature/test
   Updating 446aded..56cd211
   Fast-forward
   ```

5. 결과 -> fast-foward (단순히 HEAD를 이동)

   - `master` 브랜치의 이력이 변화하지 않았기 때문! (`feature/test` 브랜치 생성 이후에 커밋이 추가되지 않음)

   ```bash
   $ git log --oneline
   56cd211 (HEAD -> master, feature/test) Complete test.html
   ```

6. branch 삭제

   ```bash
   $ git branch -d feature/test
   Deleted branch feature/test (was 56cd211).
   ```

------

### 상황 2. merge commit

1. feature/signout branch 생성 및 이동

   ```bash
   $ git checkout -b feature/signout
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch signout.html
   $ git add .
   $ git commit -m 'Complete signout.html'
   ```

3. master 이동

   ```bash
   $ git checkout master
   ```

4. *master에 추가 commit 이 발생시키기!!*

   - 다른 branch에서 작업하지 않은 파일 수정 해주세요!

     ```bash
     $ touch .gitignore
     $ git add .
     $ git commit -m 'Add .gitignore'
     ```

5. master에 병합

   ```bash
   $ git merge feature/signout
   ```

6. 결과 -> 자동으로 *merge commit 발생*

   ```
   Merge branch 'feature/signout'
   
   # Please enter a commit message to explain why this merge is necessary,
   # especially if it merges an updated upstream into a topic branch.
   #
   # Lines starting with '#' will be ignored, and an empty message aborts
   # the commit.
   
   ```

   - Vim으로 열림! 
   - 메시지 수정하고자 하면 `i` 로 편집모드를 통해 수정하고
   - `esc` + `:` + `wq` 를 통해서 저장 및 종료
     - w : write
     - q : quit

   ```bash
   hint: Waiting for your editor to close the filMerge made by the 'recursive' strategy.
    signout.html | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 signout.html
   
   ```

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   c914a02 (HEAD -> master) Merge branch 'feature/signout'
   |\
   | * e5de8e9 (feature/signout) Complete signout.html
   * | e945f5e Add .gitignore
   |/
   * 56cd211 Complete test.html
   
   ```

8. branch 삭제

   ```bash
   $ git branch -d feature/signout
   ```

   ----

### 상황 3. merge commit 충돌

1. feature/board branch 생성 및 이동

   ```bash
   $ git checkout -b feature/board
   ```

2. 작업 완료 후 commit

   - `.gitignore` 수정

     ```bash
     $ vi .gitignore
     $ git add .
     $ git commit -m 'Edit .gitignore'
     ```

3. master 이동

   ```bash
   $ git checkout master
   ```

4. *master에 추가 commit 이 발생시키기!!*

   - 다른 branch에서 작업한 파일을 같이

   - `.gitignore` 수정

     ```bash
     $ vi .gitignore
     ```

5. master에 병합

   ```bash
   $ git merge feature/board
   ```

6. 결과 -> *merge conflict발생*

   ```bash
   $ git merge feature/board
   Auto-merging .gitignore
   CONFLICT (content): Merge conflict in .gitignore
   Automatic merge failed; fix conflicts and then commit the result.
   (master|MERGING) $
   ```

7. 충돌 확인 및 해결

   ```bash
   <<<<<<< HEAD
   *.xlsx
   =======
   *.csv
   >>>>>>> feature/board
   ```

   - 충돌 mark 를 확인하여, 코드를 알맞게 수정한다!
   - `git status` 명령어 통해서 어느 파일이 충돌인지 확인한다.

8. merge commit 진행*

   ```bash
   $ git add .
   $ git commit
   ```

   - commit 메시지는 미리 작성되어 있다!

9. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   ```

10. branch 삭제

    ```bash
    $ git branch -d feature/board
    ```

## stash - 임시 공간

> 작업 중에 작업이 완료 되지 않아서 커밋을 하기 애매한 상황에서 임시적으로 현재의 변경사항을 저장할 수 있는 공간이 있다!

1. 현재 작업 파일 stash로 이동

   * `working directory` 작업 이력을 stash로 이동시킨다.

     ```bash
     $ git stash
     ```

2. `working directory` 에 반영

   * 다시 작업 이력을 불러온다.

     ```bash
     $ git stash pop # apply + drop
     $ git stash apply # 불러오기
     $ git stash drop # 삭제하기
     ```

   * 위의 명령어는 아래의 두 개의 명령어를 실행시키는 것과 동일하다. 

3. stash 확인

   ```bash
   $ git stash list
   ```

## Reset vs Revert

### 1. Reset

> 특정 시점의 이력으로 되돌릴 수 있다.

1. 특정 시점 + 변경사항을 Staging Area

​```bash
$ git reset {커밋해시코드}
​```

2. 특정 시점

​```bash
$ git reset --hard {커밋해시코드}
​```

* Working directory에 기존의 변경사항을 남겨주지 않음!

### 2. Revert

> 특정 시점의 이력으로 돌아갔다는 커밋과 함께 되돌릴 수 있다.

​```bash
$ git revert {커밋해시코드}
​```
```

