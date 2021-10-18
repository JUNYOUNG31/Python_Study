# day 40

## DB

## Database



## SQL



## 테이블 생성 및 삭제

### DB 생성하기

```bash
$ sqlite3 tutorial.splite3
sqlite3> .database
```



### CSV 파일을 table로 만들기

```sqlite
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables 					 --확인
examples
```



### SELECT 

```sqlite
SELECT * FROM examples;               -- ; 까지 넣어야 명령이 끝난다.
```



### TIP. 터미널 뷰 변경

```sqlite
sqlite> .headers on
sqlite> .mode column

id  first_name  last_name  age  country  phone          -- headers
--  ----------  ---------  ---  -------  -------------  -- column
1   길동          홍          600  충청도      010-2424-1232 
```



### 테이블 생성 및 삭제 statement

```
* CREATE TABLE - DB에서 테이블 생성
* DROP TABLE   - DB에서 테이블 제거
```



### CREATE 

```sql
CREATE TABLE classmates (      
  id INTERGER PRIMARY KEY,       
  name TEXT
);
```



```sqlite
sqlite> CREATE TABLE classmates (      
   ...> id INTERGER PRIMARY KEY,    
   ...>  name TEXT); 
sqlite> .tables	 -- 생성 확인
classmates  examples 
```



### DROP

```sqlite
DROP TABLE classmates;  -- 테이블 삭제
```



## CRUD-CREATE

### INSERT

```sql
* 테이블에 단일 행 삽입
INSERT INTO 테이블 이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, 값3)
INSERT는 특정 테이블에 행(레코드)를 삽입(생성)
```



```sql
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 30, '서울특별시');

-- 모든 것을 명시할때는 column 을 적지않아도 됨
INSERT INTO classmates 
VALUES ('홍길동', 30, '서울특별시');
```



### SQLite 는 rowid 를 자동 관리

```sqlite
SELECT rowid, * FROM classmates;

SQLite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는
pk 옵션을 가진 rowid 칼럼을 정의
```



### NOT NULL

```sql
필요한 정보를 공백으로 비우지 안기 위해서 NOT NULL 설정을 해준다.

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
```



## CRUD-READ

### SELECT statement

```sql
* SELECT
	* 테이블에서 데이터를 조회
	* ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...
	
	* LIMIT
		* 쿼리에서 반환되는 행 수를 제한
		* 특정 행부터 조회하기 위해서는 OFFSET 키워드와 함께 사용
	* WHERE
		* 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
	* DISTINCT
		* 조회 결과에서 중복 행을 제거
		* SELECT 키워드 바로 뒤에 작성해야됨

SELECT 컬럼1, 컬럼2, ... FROM 테이블 이름
```

