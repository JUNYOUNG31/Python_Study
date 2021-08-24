# 첫 줄에는 행과 열의 크기가
# 이어서 N개의 줄에 걸쳐 입력이 주어진다.

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 1 2 3

N, M = map(int, input().split())

# 1. 빈리스트를 만들어 넣고 1차리스트를 append 하자.

# arr = []
# for _ in range(N):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# 2. 행의 공간을 미리 확보를 해두고 해당 자리를 바꾼다.
# arr = [0] * N
#
# for i in range(N):
#     arr[i] = list(map(int, input().split()))

# 3. 리스트 내포 방식

# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for i in arr:
#     print(*i)

##############################################
# N * M 크기의 0으로 가득찬 이차원배열 만들어보자..
arr = [[0]*M for _ in range(N)]

