# day8_2

## OOP

### 객체

* 객체
  * 객체(object) 는 특정 타입의 인스턴스(instance)이다.
    * 1,2,3는 int의 인스턴스
    * 'hi','bye'는 string의 인스턴스
    * [1,2,3],[]은 모두 list의 인스턴스
* 객체의 특징
  * 타입(type) 
  * 속성(attribute) 
  * 조작법(method) 



* is : 객체의 아이덴티티를 검사하는 연산자
  * type(10) is int >> True



* isinstance(object, classinfo)
  * classinfo 의 instance 거나 subclass* 인 경우 True



* 객체 -메서드(method)



* self 

  * 인스턴스 자기자신

  * ```python
    #축약형(객체지향적)
    'apple'.capitalize()
    #원래는 밑의 값이지만 capitalize(self,/) 이기때문에 위와 같이 사용가능
    str.capitalize('apple')
    ```

  * 





---

### 메서드의 종류

* 인스턴스 메서드

  * 인스턴스가 사용할 메서드

  * 클래서 내부에 정의되는 메서드의 기본

  * 호출 시, 첫번째 인자로 인스턴스 자기자신이 전달

    * ```python
      class MyClass:		   #!!!#
          def instance_method(self, arg1, ...):
      ```

    

* 클래스 메서드

  * 클래스가 사용할 메서드

  * @classmethod 데코레이터를 사용하여 정의

  * 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

    * ```python
      class MyClass:
          
          @classmethod   #self 가 아니라 cls
          def clss_method(cls, arg1, ...):
      ```



* 스태틱 메서드

  * 클래스가 사용할 메서드

  * @staticmethod 데코레이터를 사용하여 정의

  * 호출시, 어떠한 인자도(self 와 cls) 전달되지 않음(클래스 정보에 접근/수정 불가)

    * ```python
      class MyClass:
          
          @staticmethod
          def class_method(arg1, ...):
      ```

  



* 메서드 정리





* == & is
  * == 
    * 동등한(equal)
    * 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
    * 두 객체가 같아 보이지만 실제로 동일한 대상을 가르키고 있다는 것은 아님
  * is
    * 동일한(identical)
    * 두 변수가 동일한 객체를 가르키는 경우 True



---

## 클래스 / 인스턴스 / 메서드





