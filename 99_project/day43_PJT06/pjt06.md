# pjt06



## **# Git branch 실습**

```
1. branch는 단순한 포인터(화살표)다.
2. HEAD는 단순한 포인터다. (포인터의 포인터인 경우가 많다.)
3. HEAD는 현재 내가 작업중인 커밋을 의미한다.
4. HEAD가 master에 있다 == 현재 master에서 작업중이다.
5. $ git branch <name> 으로 새로운 브랜치 생성
6. $ git switch <name> 으로 새로운 브랜치 이동
```

```
# 깃의 포인터 확인
git log --oneline

# 브랜치를 현재 위칭에 생성
git branch b1

# 브랜치를 변경
git switch b1

# 브랜치를 병합
git merge b2

# 브랜치를 생성하고 생성한 브랜치로 변경
git switch -c b3 

# 그래프로 현재의 log들의 커밋을 확인
git log --oneline --graph

# 브랜치들은 merge한 후에 다시 돌아갈 일이 없다.
# 
```

```
# MERGING 중 충돌이 발생하면 
#Accept Current Change (현재 HEAD로 변경)
#Accept Incoming Change ( 충돌난 다른 브랜치로 변경)

<<<<<<< HEAD (Current Change)
secreat file <- master 브랜치에서 작성


WARNING <-master 브랜치에서 작성
=======
비밀파일입니다. <- b3 브랜치에서 작성



5번줄에 추가로 작성했습니다. <- b3 브랜치에서 작성
>>>>>>> b3 (Incoming Change)


# 변경후 git add . 와 git commit 을 다시해주면 끝
```





## Git rab 에서 실습

```
project 생성시 
Initialize repository with a README 체크

생성 후 members 추가
```


