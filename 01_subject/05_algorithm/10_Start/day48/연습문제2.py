# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해보자

# 01D06079861D79F99F

code = input()                                  # 입력
code_10 = int('0x'+code, 16)                    # 10진수로 변환
code_2 = list(bin(code_10))                     # 2진수로 변환해서 리스트화
code_2.pop(0)                                   # 앞의 0b 삭제
code_2.pop(0)
code_7 = []                                     # 7개로 나눈 리스트
# print(len(code_2))
for i in range(len(code_2)//7):                 # 2진수로 바꾼값의 길이를 7로 나눠서 반복
    code_s = []                                 # 임시 리스트
    for j in range(7):                          # 7 만큼 반복해서
        code_s.append(code_2.pop(0))            # 임시 리스트에 7개씩 추가한 리스트를
    code_7.append(code_s)                       # 7 리스트에 추가
if code_2:                                      # 다하고도 남은 값이 있다면
    x = len(code_2)                             # 길이를 구해서
    for k in range(7-x):                        # 7 - x 만큼 반복해서
        code_2.insert(0, '0')                   # 앞에 0을 추가해준다
code_7.append(code_2)                           # 그 7자리를 마지막 리스트 값으로 추가
# print(code_7)
ans = []
for i in range(len(code_7)):                    # 리스트만큼 반복해서
    hap = 0                                     # 10진수로 변환
    for j in range(len(code_7[i]), 0, -1):      # 인덱스를 뒤에서 부터 읽고
        hap += int(code_7[i][j-1])*(2**(7-j))   # 각 자리수 더하기
    ans.append(hap)                             # 정답에 추가
print(*ans)