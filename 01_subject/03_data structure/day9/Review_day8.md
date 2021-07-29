# Review_day8

## Workshop

## 1. pip

```bash
$ pip install faker
```

(1)faker 라는 패키지을 설치하기 위한 명령어 

(2) bash, cmd, shell 에서 실행한다



## 2. Basic Usages

```python
from faker import Faker # 1 faker패키지 안의 Faker 모듈 가져오기 위한 코드이다
fake = Faker()          # 2 Faker는 클래스, fake는 인스턴스이다.
fake.name()             # 3 name()은 fake의 속성이다.
```



## 3.  Localization

```python
class Faker():
    def __init__(self,locale='en_US'):
        pass
```



## 4.  Seeding the Generator

```python
fake = Faker('ko_KR')
Faker.seed(4321)
# seed()는 클래스 메소드
print(fake.name())  # 1  이도윤

fake2 = Faker('ko_KR')
print(fake2.name()) # 2  이지후
```



```python
fake = Faker('ko_KR')
fake.seed_instance(4321)
# seed_instance() 인스턴스 메소드 
print(fake.name())   # 1 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())  # 2 김광수
```





## Homework

## 1. Type Class

```python
dict() str() map() int() float()
```



## 2. Magic Method

```python
__init__    # 생성자를 생성하고
__del__     # 생성자를 삭제하고
__str__     # 문자열을 출력하고
__repr__    # 문자열을 출력하는데 해당 객체를 인간이 
			# 이해할 수 있는 표현으로 나타내기 위한 용도 랍니다...
```



## 3. Instance Method

```python
문자열

문자열.find(x)
# x의 첫번째 위치를 반환. 없으면 -1 반환
문자열.index(x)
# x의 첫번째 위치를 반환. 없으면 오류발생
문자열.strip([chars])
#특정한 문자들을 지정하면, 양쪽을 제거하거나(strip),
#왼쪽을 제거하거나(lstrip),오른쪽을제거(rstrip)
#문자열을 지정하지 않으면 공백을 제거
문자열.split(sep=none)
#문자열을 특정한 단위로 나눠 리스트로 반환
.capitalize() : 앞글자를 대문자로
.title() : '나 공백 이후를 대문자로
.upper() : 모두 대문자로
.lower() : 모두 소문자로
.swapcase() : 대<->소문자로 변경하여
.isalpha() : 알파벳 문자 여부
.isupper() : 대문자 여부
.islower() : 소문자 여부
.istitle() : 타이틀 형식 여부
    
list
```



## 4. Module Import

```python
# fibo.py
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
```

```python
from fibo import fibo_recursion as recursion
recursion(4)
```



