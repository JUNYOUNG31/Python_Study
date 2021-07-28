# 1.모음은 몇 개나 있을까?
def count_vowels(word):
    count =0 #변수 모음마다 1씩 추가
    count += word.count('a')
    count += word.count('e')
    count += word.count('i')
    count += word.count('o')
    count += word.count('u')

    return count

print(count_vowels('fineapple'))
print(count_vowels('samsung'))

# 2. 문자열 조작
# (4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를
# 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다

#=> 특정문자를 지정하지 않으면 공백을 제거한다.

# 3. 정사각형만 만들기
def only_square_area(W,H):
    area = [] #넓이
    for w in W: #너비
        for h in H: #높이
            if w == h : #같을때는 정사각형
                area += [w*h] #리스트로 저장
    
    return area 

print(only_square_area([32,55,44,50,63],[13,44,32,40,55]))