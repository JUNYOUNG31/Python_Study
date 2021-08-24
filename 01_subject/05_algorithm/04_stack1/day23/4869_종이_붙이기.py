# 종이 붙이기
T = int(input())                 # 입력 T
square = [0] * 31                # 31 빈 배열
square[1] = 1                    # 1의 값
square[2] = 3                    # 2의 값 입력 (index 에러 방지)
for tc in range(1, T+1):         # case 반복
    N = int(input()) // 10       # 입력
    for i in range(3, 31):       # 3부터 시작
        square[i] = square[i - 1] + square[i - 2] * 2
    print(f'#{tc} {square[N]}')  # 출력


#  d[i] =>
# 한칸짜리 로 만드는 개수 1
# 두칸짜리 로 만드는 개수 2
#
# d[i-1] 에서 d[i]이 될려면 1칸짜리니깐 앞의 개수랑 같으므로 + d[i-1]
#
# d[i-2] 에서 d[i]이 될려면 2칸짜리를 더하는경우 = d[i-2] * 2
#
# d[i] = d[i-1] + d[i-2]* 2
