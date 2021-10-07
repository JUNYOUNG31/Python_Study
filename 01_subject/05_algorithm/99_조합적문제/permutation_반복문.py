#원소의 개수만큰 반복문과 조건문이 필요함.
#그러니 쓸일 없음 손목 베리 아오치

# arr = [1,2,3]
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1 :
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2 :
                    print(i1, i2, i3)
