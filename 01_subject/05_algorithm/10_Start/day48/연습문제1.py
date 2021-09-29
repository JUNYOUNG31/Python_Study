# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기

# 0000000111100000011000000111100110000110000111100111100111111001100111
# 편의상 10개 단위로 간격을 두었음. 이어있는 데이터로 간주하시오.

code = list(str(input()))                       # 리스트화

code_7 = []                                     # 7자리로 나눈 리스트
for i in range(len(code)//7):                   # 길이를 7로 나눈 만큼 반복
    code_s = []                                 # 임시 리스트
    for j in range(7):                          # 7만큼 반복    
        code_s.append(code.pop(0))              # 
    code_7.append(code_s)                       # 7자리 수로 리스트 담기
# print(code_7)
ans = []                                        # 정답 리스트
for i in range(len(code_7)):                    # 반복
    hap = 0                                     # 10진수로 변환
    for j in range(len(code_7[i]), 0, -1):      # 인덱스를 뒤에서 부터 
        hap += int(code_7[i][j-1])*(2**(7-j))   # 각자리의 값을 10진수로 바꿔서 더하기
    ans.append(hap)                             # 정답에 추가
print(*ans)




