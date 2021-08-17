### atoi 문자열을 정수로

def atoi(str_input : str) -> int:
        ans = 0

        for i in range(len(str_input)):
                ans *= 10
                ans += ord(str_input[i]) - ord('0')
                # ord(str_input[i]) - 48

        return ans

num = atoi("1234")
print(type(num), num)

def itoa(int_input: int) -> str:
        ans=''
        tmp = int_input

        # 이와 같이 작성을 하였다면 뒤집어서 결과가 나온다.
        # ( ans+=chr(num + 48) =>> ans = chr(num + 48) + ans
        while tmp > 0:
                num = tmp % 10
                ans += chr(num + 48)
                tmp //= 10
        return  ans

text =itoa(1234)
print((type(text), text))