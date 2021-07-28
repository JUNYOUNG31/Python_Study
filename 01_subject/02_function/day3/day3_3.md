# day3_3

## 함수

### 재귀 함수

자기 자신을 호출하는 함수



팩토리얼

반복문으로 만든 팩토리얼

```python
def fact(n):
    total=1
    for i in range(1,n+1):
        total *=i
    return total
        
```

재귀를 이용한 팩토리얼

```python
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
```



피보나치

```python
def fib(n):
    # base case
    if n < 2 :
        return n
    else:
        return fib(n-1) + fib(n-2)
```



## 에러 / 예외 처리

### 디버깅

에러 메세지가 발생하는 경우 

해당 하는 위치를 찾아 해결할 수 있다

---

### 에러

Syntax Error  문법 에러

파이썬 프로그램은 실행되지 않음

문제가 발생한 위치를 표현

invalid syntax

assign to literal

End of Line

End of File

----

### 예외

실행 중 감지되는 에러들을 예외라고 한다

모든 내장 예외는 Exception Class를 상속받아 이뤄짐



예외의 종류

ZeroDivisionError : 0으로 나누고자 할 때 발생

NameError : namespace 상에 이름이 없는 경우

TypeError : 타입 불일치 

​					 argument 누락

​					 argument 개수 초과

​					 argument type 불일치

ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우

IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우

KeyError : 해당 키가 존재하지 않는 경우

ModuleNotFoundError : 존재하지 않는 모듈을 import 하는 경우

ImportError - Moudle은 있으나 존재하지않는 클래스/함수를 가져오는 경우

KeyboardInterrupt : 임의로 프로그램을 종료하였을 때

IndentationError : Indentation이 적절하지 않은 경우



파이썬 내장 예외(built-in-exceptions)

---

### 예외 처리

try문 / except 절 을 이용해서 예외 처리

```python
try:
    num = inpput('숫자입력 :')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
```

복수의 예외처리

에러 별로 별도의 에러처리 가능

Exception 은 가장 큰 범주



try : 코드를 실행

except : try 문에서 예외가 발생 시 실행

else : try 문에서 예외가 발생하지 않으면 실행

finally : 예외 발생 여부와 관계없이 항상 실행



에러 메시지 처리

as 키워드를 활용해서 원본 에러 메시지를 사용가능

---

### 예외 발생 시키키

raise 를 통해 강제로 발생

raise <표현식> (메세지)

<표현식> : 예외 타입 지정(주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴)



assert 를 통해 강제로 발생

일반적으로 디버깅 용도로 사용

assert <표현식> (메세지)

<표현식> : False 인 경우 무조건  Assertion Error 