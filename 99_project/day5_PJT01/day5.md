# day5

## 관통 프로젝트_01

### CLI

start : 파일 실행

mkdir : 디렉토리 생성 (폴더 생성)

touch: 파일 생성

cd 경로 이동

.. 상위 폴더

rm <파일 이름> 삭제(완전삭제) 

rm -rf <파일 이름>



### Git

Local repo : 로컬 저장소



Directory(폴더) : 아무 기능 없음  =>git init=> Repository(저장소) : 내부의 모든 파일/폴더를 관리

$ git init

( home 폴더에서 초기화 하지 않는다)

(repo 안에 repo를 만들지 않는다 = git init 한 폴더안에 git init 하지 않는다)



repo

작업 공간       : Working directory   코드 작성 및 수정

git add

스테이지        : Staging area             기록된 파일들의 변경사항들을 스테이지에 올리기

git commit -m '메세지'

(중요) 저장소 : commits                    스테이지 위의 변경사항들을 저장

git log



git status



첫번째 커밋은 중요 - 보통 first commit 이라고 메세지를 남긴다.





git 과 연결하기

git remote add <name> <url>

git push <name> <branch>

git pull <name><branch>