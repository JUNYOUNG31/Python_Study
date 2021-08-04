# 1. pip

# bash $ pip install faker
# (1)faker 라는 패키지을 설치하기 위한 명령어 
# (2) bash, cmd, shell 에서 실행한다



#2. Basic Usages
from faker import Faker # 1 faker패키지 안의 Faker 모듈 가져오기 위한 코드이다
fake = Faker()          # 2 Faker는 클래스, fake는 인스턴스이다.
fake.name()             # 3 name()은 fake의 속성이다.

# 3.  Localization
class Faker():
    def __init__(self,locale='en_US'):
        pass

# 4.  Seeding the Generator
fake = Faker('ko_KR')
Faker.seed(4321)
# seed()는 클래스 메소드
print(fake.name())  # 1  이도윤

fake2 = Faker('ko_KR')
print(fake2.name()) # 2  이지후

fake = Faker('ko_KR')
fake.seed_instance(4321)
# seed_instance() 인스턴스 메소드 
print(fake.name())   # 1 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())  # 2 김광수