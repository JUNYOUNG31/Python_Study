# Project_03

## 반응형 웹 페이지 구성

### 1.목표

* HTML을 통한 웹 페이지 마크업 분석
* CSS 라이브러리의 이해와 활용
* 컴포넌트 및 그리스 시스템 활용
* 커뮤니티 서비스 반응형 레이아웃 구성



## A. 01_nav_footer

```html
<nav class="navbar navbar-expand-md navbar-dark sticky-top bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="02_home.html">
        <img src="./images/logo.png" alt="" width="100px" height="40px">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-md-0">
            <li class="nav-item ">
            <a class="nav-link active" aria-current="page" href="02_home.html">Home</a>
          </li>
```

* 학습한 내용

  * 상단 고정
    * flexed-top , sticky-top
  * md 사이즈에서 햄버거 기능 이용
    * navbar-expand-md
    * mb-md-0
  * 강조하기
    * nav-link active
  * 하단 고정
    * flexed-bottom, sticky-bottom

* 느낀점

  * 햄버거 버튼으로 교체되는 과정에서 md 를 어디에 적용해야 할지 몰라서 시간이 지체되었다.
  * 상단고정을 flex-top으로 하니 home에서 이미지가 가려지는것 같아서 sticky-top으로 공간을 확보하여 이미지를 가리지 않도록 설정했다.
  * 강조하기를 적용하여 해당 페이지가 어딘지 확인할 수 있는것 같다.



## B. 02_home

```html
<header>
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="./images/header1.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="./images/header2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="./images/header3.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
    </div>
</header>

<section class="row row-cols-1 row-cols-sm-2 g-4">
    <article class="col">
    <article class="col">
    <article class="col">
    <article class="col">
    <article class="col">
    <article class="col">
```

* 학습한 내용

  * 강조하기
    * nav-link active
  * home 페이지 이미지 전환 기능
    * Carousel 기능 사용
  * grid 사용
    * row 와 row-cols-1, row cols-sm-2 , g-4

* 느낀점

  * Carousel 기능을 처음 사용해봤는데 자주 사용하게 될 것 같다.
  * grid 기능을 사용해서 페이지 크기에 따라 몇개를 표시할지를 정해주는것





## C. 03_Community

```html
<style>
    @media (max-width: 991px) {
  .table--none {display: none}
    }
    @media (min-width: 992px) {
  .article--none {display: none}
    }
</style>

<div class="main row m-4">
    <h1 class="text-center mb-4">Community</h1>
    <!-- Sidebar -->
    <aside class="list-group col-12 col-lg-2">
        

<section class="col-12 col-lg-10">
      <div>
        <table class="table table-striped table--none">
        </table>
      </div>  
    
      <div>
        <article class="article article--none my-4">
          <div>
            <hr>
            <div class="d-flex ustify-content-between">
              <h5>Best Movie Ever</h5> 
              <p class="ms-auto">user</p>
            </div>            
            <p>Great Movie title</p>            
            <p>1 minutes ago</p>            
          </div>          
        </article>
      </div> 
    
      <div class="d-flex justify-content-center my-4">
      </div>
</section>        
        
```

* 학습한 내용

  * 강조하기
    * nav-link active
  * 화면 전환에 따라 display 여부를 결정하게 설정
    * media query 사용하여 display : none 설정
  * grid 사용
    * row 와 col 의 설정
  * 표를 글자로 변경
    * 글을 4줄로 만들고 2줄을 flex로 변경해서 2줄을 표현

* 느낀점

  * Carousel 기능을 처음 사용해봤는데 자주 사용하게 될 것 같다.

  * grid 기능을 사용해서 페이지 크기에 따라 몇개를 표시할지를 정해주는것

  * @media (min-width: 992px)

    @media (max-width: 992px)

    이둘을 적용했을때 둘다 최대와 최소 이므로 중간의 992px 부분이 텅비는 현상이 발생했다.

    README에서 원하는 조건으로 설정하기 위해 @media (min-width: 991px) 로 설정해서 중간에 비는 부분을 채워줬다.



* 전반적으로 생소하다보니깐 익숙해지는데 시간이 좀 걸렸다. 그래도 시간안에 마무리 했다는 점에서 만족스럽다.