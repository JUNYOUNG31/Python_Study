# 이진탐색
def binarySearch(a, key):               # 2진 탐색 함수
    start = 1                           # 시작은 1페이지
    end = a                             # 끝 페이지
    cnt = 0                             # 2진 탐색한 횟수
    while start <= end:                 # 1부터 400까지
        middle = int((start + end)/2)   # c= int((l+r)/2)
        cnt += 1                        # 카운트 1 증가
        if middle == key:               # 그값이 같다면
            return cnt                  # 횟수 반환
        elif middle > key:              # 중간값이 찾는 값보다 크면
            end = middle                # 끝값이 중간값
        else:                           # 중간값이 찾는 값보다 작으면
            start = middle              # 시작값이 중간값
    return cnt                          # cnt 반환


T = int(input())                                        # case 수
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())               # 페이지수 , 찾는값 A, 찾는값 B
    ans = ''                                            # 정답
    if binarySearch(P, Pa) < binarySearch(P, Pb):       # 횟수가 B가 더크면
        ans = 'A'                                       # A가 이김
    elif binarySearch(P, Pa) > binarySearch(P, Pb):     # A가 크면
        ans = 'B'                                       # B가 이김
    elif binarySearch(P, Pa) == binarySearch(P, Pb):    # 같으면
        ans = '0'                                       # 0 반환

    print("#{} {}".format(tc, ans))