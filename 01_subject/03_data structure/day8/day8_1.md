# day8_1

## 모듈

### 모듈과 패키지

* 모듈
  * 특정 기능을 파이썬 파일 단위로 작성한 것



* 패키지
  * 특정 기능과 관련된 여러 모듈의 집합
  * 패키지 안에서 또 다른 서브 패키지를 포함



* 파이썬 표준 라이브러리
  * 파이썬에 기본적으로 설치된 모듈과 내장 함수
  * ex) random.py



* 파이썬 패키지 관리자(pip)

  * PyPI에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

    ex) requests , beautiful soap

    * 설치 : pip install requests 

    * 삭제 : pip uninstall requests

    * 설치된 항목 : pip list

    * 설치된 항목의 정보 :pip show [SomePackage]

    * 패키지 관리하기 

      패키지 목록을 관리[1]하고 설치할 수 있음[2]

      * [1] pip freeze > requirements.txt

      * [2] pip install -r requirements.txt

        다른 컴퓨터에 똑같은 환경을 설치하고 싶을때 사용한다.

      * github에서 파이썬 프로젝트를 할때 requirements.txt 을 함께 올려줘서

        다른 사용자가 같은 환경을 다룰수 있음



---

### 가상환경

* 가상환경

  * 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우

    모두 pip를 통해 설치해야함

  * 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    * [1] 프로젝트 - django 버전 2.x
    * [2] 플로젝트 - django 버전 3.x
  * 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음



* venv 
  * 가상환경을 만들어 관리하는데 사용되는 모듈
  * 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    * 특정 폴더에 가상 환경이(패키지 집합 폴더) 있고
    * 실행 환경(-bash)에서 가상환경을 활성화 시켜
    * 해당 폴더에 있는 패키지를 관리/사용



* 가상환경 생성

  * 가성환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치

    * $ python -m venv <폴더명>  이지만 폴더명을 venv 로 통일
    * $ source venv/Scripts/activate  : 가상환경 활성화
    * $ pip list 로 확인
    * $ deactivate : 가상환경 비활성화

  * 폴더마다 실행이 되는것이 아니라 ON OFF 개념이라서 폴더를 빠져나와도 유지

  * 가상환경이 활성화 된 이후에 $ which python 명령어를 사용하면

     현재 활성화 된 파이썬 가상환경의 위치가 출력



---

### 모듈/패키지 활용하기

* 모듈 만들기 -check
  * check.py 에 짝수를 판별하는 함수 even 과 홀수를 판별하는 함수 odd 를 만든다
* 모듈 활용하기 -check
  * import check 를 하면  
    * check.odd()  , check.even() 과 같이 사용가능
  * from check import odd
    * odd 만 사용 가능 even 사용 불가
  * from check import *   ( 하지만 * 권장하지 않는다)
    * odd , even 사용가능



* 패키지

  * 패키지는 여러 모듈/하위 패키지로 구조화

    * ex) package.module

  * 모든 폴더에는  __ init __.py 를 만들어 패키지로 인식 

    Python 3.3 부터는 파일이 없어도 되지만, 하위 버전의 호환을 위해 생성하는 것을 권장



* 패키지 만들기

  * 수학과 통계 기능이 들어간 패키지를 구성

    * math의 tools : 자연 상수 e , 원주율 pi 값, 최댓값 my_max 함수

    * statistics의 tools : 평균을 구하는 mean 함수

      * ```python
        my_package/
        	__init__.py
        	math/
        		__init__.py
        		tools.py
        	statistic/
        		__init__.py
        		tools.py
        ```

        

    





