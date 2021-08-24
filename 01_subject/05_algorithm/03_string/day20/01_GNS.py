# GNS
import sys
sys.stdin = open("GNS_test_input.txt", "r")


# print(type(alpha1))
# print(alpha["TWO"])

T = int(input())
# T = 10
for test_case in (1, T+1):
    N = list(input().split())
    # print(N)
    arr = list(input().split())
    # print(arr)
    count = len(arr)
    # print(count)

    # 딕셔너리로 키와 값으로 매칭시킬거다
    alpha = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    number = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    for i in range(count):  # 인덱스범위만큼 반복문 돌리고
        arr[i] = alpha[arr[i]] # 해당 키에 대한 값을 넣는다.
        # print(arr)

    # 정렬을 위해 버블정렬할것이다  # 함수만 쓸 수 있으면 sort쓸건데
    for j in range(len(arr)-1, 0, -1):
        for k in range(0, j):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    # print(arr)

    # arr.sort()

    # 여기서 숫자 키에 맞는 값을 매칭한다
    for l in range(count):
        arr[l] = number[arr[l]]

    print("#{} {}".format(test_case, ' '.join(arr)))