# 1. Circle 인스턴스 만들기
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumference(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x , self.y)

cir1 = Circle( 3 , 2, 4)
print(cir1.area())
print(cir1.circumference())


#  2. Dog 와 Bird 는 Animal 이다
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def __init__(self,name):
        self.name = name

    def fly(self):
        print(f'{self.name}! 푸드덕!')



dog = Dog('멍멍이')
dog.walk() # 멍멍이! 달린다!
dog.bark() # 멍멍이! 짖는다!

bird = Bird('구구')
bird.walk() #구구! 걷는다!
bird.eat() #구구! 먹는다!
bird.fly() #구구! 푸드덕!

# 3. 오류의 종류
# ZeroDivisionError : 0으로 나누면 발생
# NameError :이름이 연결되어 있지 않으면 예외 발생
# TypeError :대입되는 값이 다른 형식일 경우 발생
# IndexError :찾는 위치가 범위를 벗어나면 발생
# KeyError  : 찾는 키가 범위를 벗어나면 발생
# ModuleNotFoundError : ImportError 의 서브 클래스인데, 모듈을 찾을 수 없을 때 발생
# ImportError : import 문이 모듈을 로드하는 데 문제가 있을 때 발생 \
#               from ... import 에서 임포트 하려는 이름을 찾을 수 없을 때도 발생