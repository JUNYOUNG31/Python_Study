#List의 합 구하기
 # => 15
def list_sum(i):
    total = 0
    for a in i:
        total += a
    return total

print(list_sum([1,2,3,4,5]))

#Dictionary로 이루어진 lsit의 합 구하기
def dict_list_sum(i):
    total = 0
    for a in i:
        total += a['age']
    return total

print(dict_list_sum([{'name': 'kim', 'age': 12},
                     {'name': 'lee', 'age': 4}])) #=> 16