# day 31

## django Model



### Model

* 단일한 데이터에 대한 정보를 가짐
  * 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
* 저장된 데이터베이스의 구조(layout)



### Database

* 데이터베이스(DB)
  * 체계화된 데이터의 모임
* 쿼리(Query)
  * 데이터를 조회하기 위한 명령어
  * 조건에 맞는 데이터를 추출하거나 조작하는 명령어
* 스키마(Schema)
  * 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
* 테이블(Table
  * 필드 / 컬럼 / 속성
  * 레코드 / 행 / 튜플



### DB 의 기본구조

* 스키마, 테이블, 칼럼, 레코드, PK(기본키)



## ORM

### ORM 

* Object Relational Mapping

* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에(Djang0-SQL)데이터를 변환하는

  프로그래밍 기술

* OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의

  호환되지 않는 데이터를 변환하는 프로그래밍 기법

* Django는 내장 Django ORM을 사용



* 장점

  * SQL을 잘 알지 못해도 DB 조작이 가능
  * SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

* 단점

  * ORM 만으로 완전한 서비스를 구현하기 어려움

* 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는것 ==> 생산성

  

```
# 폴더 생성
$ mkdir 01_django_model

# 폴더로 이동
$ cd 01_django_model

#폴더안에서 가상환경 설정
$ python -m venv venv

#가상환경 활성화
$ source venv/Scripts/Activties

# jango 설치
$ pip install django

# 프로젝트 생성
$ django-admin startproject crud

# 프로젝트의 앱 생성
$ python manage.py startapp articles
```



### 사용 모델 필드

* CharField
