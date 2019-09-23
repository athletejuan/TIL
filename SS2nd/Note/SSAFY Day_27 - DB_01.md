# DataBase

## SQL



테이블에 데이터 삽입(새로운 행 추가) -> Insert

데이터삭제 -> Delete

데이터수정 -> Update

데이터선택 -> Select



#### WINDOW 에서 sqlite 사용

sqlite download

sqlite 폴더만들어서 다운받은 파일 압축풀고 총 5개의 파일을 (하나의 폴더에) 이동

sqlite3.dll 파일의 경로 확인 (Macintosh HD⁩ ▸ ⁨Users⁩ ▸ ⁨juan⁩ ▸ ⁨GIT⁩ ▸ ⁨TIL⁩ ▸ ⁨Web⁩ ▸ ⁨04_django⁩ ▸ ⁨EXERCISE⁩ ▸ ⁨sqlite⁩)

(환경변수에 추가) 사용자 변수 / path 에 새로만들기 / 위의 파일 경로 Ctrl+C,V

Git bash 껐다켜서

winpty sqlite3 (단축키 설정하기)

- ~ (vscode 킴)

- source ./.bashrc

- alias sqlite3='winpty sqlite3'

(기타 단축키)

- jn="jupyter notebook"

- venv="source ./venv/bin/activate"

- rs="python manage.py runserver"



winpty sqlite3 db.sqlite3

$ .exit

$ .databases

$ SELECT * FROM board_article;

zzu.li/hello.db



$ sqlite3 tutorial.sqlite3

$ .mode csv

$ .import hellodb.csv examples

$ .tables

examples

$ SELECT * FROM examples;

$ .headers on

$ SELECT * FROM examples;

$ .mode column

$ SELECT * FROM examples;



$ CREATE TABLE classmates(

id INTEGER PRIMARY KEY,

name TEXT

);

$ .tables 



$ .schema table

$ DROP TABLE examples;

$ CREATE TABLE classmates(

name TEXT,

age INT,

address TEXT,

);

$ .schema classmates

.tables



INSERT INTO table (column1, column2, ...)

VALUES(value1, value2, ...)

$ INSERT INTO classmates(name, age) VALUES('홍길동', 23);

$ SELECT * FROM classmates

중복된 값이 들어갈 경우(중복값 들어갈 수 있다.)

SELECT rowid, * FROM classmates; (rowid 로 구분가능)



#### LIMIT

위에서부터 해당 갯수만큼의 데이터만 가져옴(1개의 데이터만 가져올때 유용함.)

LIMIT num1 OFFSET num2

num2 이후부터 num1개의 데이터 가져옴()



#### WHERE

WHERE column=value;

$ SELECT * FROM classmates(table명) WHERE id(column명)=3(value);



#### DELETE

DELETE FROM table WHERE condition;

중복될 수 있는 조건을 기준으로 삭제하면 중복항목 가진 모든 데이터 삭제됨.



게시글 과 댓글 여러개가 있는 글의 경우

게시글을 지우더라도 DB에서 실제로 삭제하지 않는 경우가 많음

게시글 지우고 다시 그 행에 새로운 데이터를 넣으려 하는 경우

게시글 정보와 댓글 정보가 겹칠 수 있음.

(ID, PW의 경우 심각한 문제 발생 가능)



#### AUTOINCREMENT (데이터 삭제 후 해당행에 데이터를 새로 입력하는 것을 방지)

CREATE TABLE tests(

** id INTEGER PRIMARY KEY AUTOINCREMENT, **

name TEXT NOT NULL);



#### UPDATE

UPDATE table SET column1=value1, column2=value2,.... WHERE condition;



$ SELECT COUNT(*) FROM classmates; (항목 갯수)



#### LIKE(wild cards)

_ : 반드시 한자리 있어야 함

% : 한자리 있어도, 없어도 됨

FROM classmates WHERE age LIKE 2_;



#### ALTER(테이블명 변경)

$ ALTER TABLE users2(exist_table) RENAME TO users(new_table);

$ .tables

 새로운 컬럼 추가

$ ALTER TABLE table ADD COLUMN created_at DATETIME NOT NULL

기존 데이터들은 NULL 값이므로 DEFAULT 값을 설정해주어야 함.

$ ALTER TABLE table ADD COLUMN gender TEST NOT NULL DEFAULT 'male';

