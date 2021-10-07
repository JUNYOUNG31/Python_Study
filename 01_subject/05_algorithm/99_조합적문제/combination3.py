# 3개 정도의 조합은 반복문으로 짜는 경우도 수두루 뺵뺵하다.


N = 4
# R = 3
arr = [1, 2, 3, 4]
#시작과 끝인덱스를 잘 봐두자.!!!!!!
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            print(arr[i], arr[j], arr[k])
