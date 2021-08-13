# 문자열 뒤집기

word = '삼성청년소프트웨어아카데미'

# 1. 뒤에서부터 읽기
for i in range(len(word)-1, -1, -1):
    print(word[i], end='')
print()

# 2. 슬라이싱 사용
print(word[::-1])

# 3. reverse 함수
print(''.join(reversed(word)))

# 4. swap 방법
N = len(word)
swap_word = list(word)
for i in range(N // 2):
    swap_word[i], swap_word[N-i-1] = swap_word[N-i-1], swap_word[i]
print((''.join(swap_word)))