# 1. pip 

# bash 에서 $ pip install faker

# 2. Basic Usages
from faker import Faker # 1 모듈을 사용하기 위한 코드이다
fake = Faker()          # 2 Faker는 클래스, fake는 인스턴스이다.
fake.name()             # 3 name()은 fake의 속성이다.

# 3. Localization

fake = Faker()
fake.name()
# => 'shelly wilcox' (랜덤이므로 결과 값이 다를 수 있음)

fake_ko = Faker('ko_KR')
fake_ko.name()
# => '박진우' (랜덤이므로 결과 값이 다를 수 있음)

class Faker():
    def __init__(self,fake):
        pass


# 4. Seeding the Generator
import random

random.random() #=> 임의의 수
random.random() #=> 임의의 수

random.seed(7777) 
random.random() # => 0.8170477907294282

random.seed(7777) 
random.random() # => 0.8170477907294282

fake = Faker('ko_KR')
Faker.seed(4321)  # 클래스 메소드

print(fake.name())  # 1

fake2 = Faker('ko_KR')
print(fake2.name()) # 2 

# 4. Seeding the Generator
fake = Faker('ko_KR')
fake.seed_instance(4321) # 인스턴스 메소드 

print(fake.name())   # 1

fake2 = Faker('ko_KR')
print(fake2.name())  # 2