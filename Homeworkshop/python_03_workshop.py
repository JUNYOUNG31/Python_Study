#List의 합 구하기
def list_sum(i):
    total = 0
    for a in i:
        total += a
    return total

print(list_sum([1,2,3,4,5,6]))

#Dictionary로 이루어진 lsit의 합 구하기
def dict_list_sum(i):
    total = 0
    for a in i:
        total += a['age']
    return total

print(dict_list_sum([{'name': 'kim', 'age': 18},
                     {'name': 'park', 'age': 6}])) 

#2차원 list의 전체 합 구하기
def all_list_sum(i):
    total =0
    for a in i:
        if type(a) == list:
            total += all_list_sum(a)
        else:
            total += a
    return total

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]))