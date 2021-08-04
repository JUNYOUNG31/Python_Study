# 1. 평균 점수 구하기
def get_dict_avg(subject):
    hap = 0
    for i in subject:
        hap += subject[i]
    return hap / len(subject)

print(get_dict_avg({
    'python':60,
    'algorithm':70,
    'django':89,
    'web':85
}))

# 2. 혈액형 분류하기
def count_blood(list_Blood):
    detail={
        'A' : list_Blood.count('A'),
        'B' : list_Blood.count('B'),
        'O' : list_Blood.count('O'),
        'AB' : list_Blood.count('AB')
    }
    return detail

print(count_blood([
    'A','B','AB','O','AB','A',
    'O','O','B','A','B','B'
]))