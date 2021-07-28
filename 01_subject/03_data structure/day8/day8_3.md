# day8_3

## 상속

### 상속

* 클래스는 상속이 가능

  * 모든 파이썬 클래스는 object를 상속 받음

* 상속을 통해 객체 간의 관계를 구축

* 부모 클랫의 속성, 메서드가 자식 클래스에 상속되므로 코드 재사용성이 높아짐

* ```python
  class ChildClass(ParentClass):
  ```



---

### 상속 isinstance

* isinstance(object, classinfo)
  * classinfo 의 instance거나 subclass*인 경우 True



### issubclass

* issubclass(class, classinfo)
  * class가 classinfo의 subclass면 True
  * classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목 검사



### super()

* 자식클래스에서 부모클래스를 사용하고 싶은 경우



### 메서드 오버라이딩(method overriding)

* 상속 받은 메서드를 재정의
  * 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
  * 부모 클래스의 메서드를 실행시키고 싶은 경우 super 활용



---

### 상속 정리



파이썬의 모든 클래스는 object로부터 상속

부모 클래스의 모든 요소(속성, 메서드)가 상속

super()를 통해 





### 다중 상속

* 두 개 이상의 클래스를 상속 받은 경우 다중 상속
  * 상속 받은 모든 클래스의 요소를 활용 가능
  * 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정







