# day11

## web

## HTML



Hyper Text Markup Language





태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

프로그래밍 언어와는 다르게 단순하게 데이터를 표현하기만 한다.



웹페이지를 작성하기 위한(구조를 잡기 위한) 언어

웹 컨텐츠의 '의미'와 '구조'를 정의



기본 구조

head 요소



body 요소

브라우저 화면에 나타나는 실제 정보





메타 데이터를 표현하는 새로운 규약 open graph protocol : og



DOM(Document Object Model) 트리



---

### 요소(element)

```html
		<h1>contents</h1> 
(여는/시작) 태그       (닫는/종료)태그
```

HTML의 요소는 태그와 내용으로 구성

요소는 중첩될 수 있음



### 속성(attribute)

```html
   속성명      속성값
<a href="https://google.com"
   	   공백은 No!			""(쌍따옴표) 사용
```

요소의 시작 태그에 작성

이름과 값이 하나의 쌍으로 존재

태그와 상관없이 사용 가능한 속성도 있음



<!-- -->

a = 하이퍼 링크





시맨틱 태그

의미 있는 정보의 그룹을 태그로 표현

단순 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용

Non semantic 요소는 div , span

h1, table 태그들도 시맨틱 태그로 볼수 있음



시맨틱 웹





## HTML 문서 구조화

### 인라인 / 블록 요소

그룹 컨텐츠

```
<p>
<hr>
<ol>, <ul>
<pre>, <blockquote>
<div>
```

텍스트 관련 요소

```
<a>
<b> vs <strong>
<i> vs <em>
<span>, <br>, <img>
```

table  : 잘 사용하지 않는다



form : 가장 중요한 태그

```
서버에서 처리될 데이터를 제공
<form> 기본 속성
action
method
```



input

다야한 타입을 가지는 입력 데이터 필드

```
<label> : 서식 입력 요소의 캡션
<input> 공통 속성
name , placeholder
required
autofocus
```



input type 

submit 제출

---

### 마크업 해보기

구조

1. header
2. section
   * action 은 반드시 있어야 한다
3. footer



## CSS

Cascading Style Sheets



### CSS 정의 방법 - 1(인라인)

해당 태그에 직접 style 작성



### CSS 정의 방법 - 2(내부 참조)

head 태그 내에 <style>에 지정



### CSS 정의 방법 - 3(외부 참조)

외부 css 파일을 <head>내 <link> 를 통해 불러오기





