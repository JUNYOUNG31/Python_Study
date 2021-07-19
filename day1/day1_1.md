# day1_1

## Python 기초

### 기초 문법

코드 스타일 가이드 

PEP8  파이썬에서 제안하는 스타일 가이드   = 파이썬 사용에서 문법

주석   

한줄 주석 # ,   여려줄 주석 ```, """  >>> docstring

여러줄 주석 드래그 ctrl + /  

docstring 함수/ 클래스의 설명 작성

주석을 적고

```
ex.__foc__
하면 밑에줄에 주석을 알려준다.
```



---

### 변수와 식별자

=          할당 연산자

같은 값을 동시에 할당 가능   x = y = 1004

다른 값을 동시에 할당 가능   x , y = 1, 2

type()   할당된 타입 확인

id()        메모리 주소 확인

---

### 데이터 타입

숫자  

int

float

complex



문자열  string



참 거짓 boolean



none

---

### 타입변환

암시적 타입 변환

```
true + 3 = 4 >>> int
3 + 4.0 = 7.0 >>> float
3 + 4j + 2 = 5 + 4j >>> complex
```

명시적 타입 변환

int

str , float >>> int

str , int >>> float

int , float , list , tuple , dict >>> str

```
ex) '3' + 4 >>Error  # 암시적 X
ex) int('3') + 4 = 7 # 명시적 
```

---

### 연산자

산술   // 몫  ** 거듭제곱



비교   is     is not



논리   A and B , A or B , Not    일반적으로 비교연산자와 사용

and 연산에서 첫번째 값이 False 이면 무조건 False >>> 첫번째값 반환

or  연산에서 첫번쨰 값이 True 이면 무조건 True >>> 첫번쨰 값 반환

```
a = 5 and 4
print(a)
>>> 4
b = 5 or 3
print(b)
>>> 5

c = 0 and 5
print(c)
>>> 0
```



복합

1씩 증가

```
cnt += 1  >>> cnt = cnt + 1
```



기타

concatenation

문자열도 + 가능 

containment test

```
'a' in 'apple' >>> true
```

identity

is 연산자로 동일한 객체인지 확인

```
# 파이썬에서 -5 부터 256까지 숫자의 id 는 동일
a = 3
b = 3
print(a is b)
print(id(a), id(b))
True
2383129307504 2383129307504

c = 257
d = 257
print(c is d)
print(id(c), id(d))
True
2921161468304 2921161468304
```

​	indexing/slicing

```
'hello, jun'[0]
'h'
'hello, jun'[1:5]
'ello'
```

연산자 우선순위

()

slicing

indexing

**

---

### 표현식/문장

표현식 평가되고 값으로 변경 하나의 값으로 환원될수 있는 묹아

식별자 , 값, 연산자로 구성



문장

파이썬이 실행 가능한 최소한의 코드 단위



모든 표현식은 문장이다  

---

