# 도형 만들기
class Point:                    # 좌표의 함수
    def __init__(self, x , y):  # 점의(x,y) 좌표
        self.x = int(x)         # int 값으로 변경
        self.y = int(y)         # int 값으로 변경

class Rectangle(Point):         #사각형의 함수
    def __init__(self,p1,p2):   # 2개의 점의 좌표
        self.p1 = p1            # p1 점1
        self.p2 = p2            # p2 점2

    def get_area(self):         # 넓이를 구하기
        return abs((self.p1.x - self.p2.x)*(self.p1.y-self.p2.y))
               #절대값으로 양의 값으로 변환 한뒤에 좌표들의 차이만큼 곱한다
    def get_perimeter(self):    # 둘레 구하기
        return abs((self.p1.x - self.p2.x))*2+ abs((self.p1.y-self.p2.y))*2
               #절대값으로 양의 값으로 변환 한뒤에 가로*2 + 세로*2
    def is_square(self):        # 정사각형인지 판별
        if abs((self.p1.x - self.p2.x)) == abs((self.p1.y-self.p2.y)):
           #절대값으로 양의 값으로 변환 한뒤 가로 세로 값이 같은지 판별
            return True
        else:
            return False

p1 = Point(1, 3)
p2 = Point (3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 8)
p4 = Point (6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
