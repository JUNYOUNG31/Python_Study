# 1. 평균 점수 구하기
def get_dict_avg(subject):
	return sum(subject.values())/len(subject.keys())

def get_dict_avg2(subject):
    hap = 0
    for score in subject.values():
        hap += score
    return hap / len(subject)

subject_values ={'python':60,'algorithm':70,'django':89,'web':85}
print(get_dict_avg(subject_values))
print(get_dict_avg2(subject_values))
	          

# 2. 혈액형 분류하기
blood = ['A','B','AB','O','AB','A','O','O','B','A','B','B']
def count_blood(list_Blood):
    blood_dict = {}
    for blood in list_Blood :
        if blood_dict.get(blood): #인덱스를 쓸경우 위에 빈딕션너리를 설정해놔서 									  #keyError가 발생한다.
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1

def count_blood2(list_Blood):
    blood_dict = {}
    for blood in list_Blood :
        blood_dict[blood] = blood_dict.get(blood,0)+1
        								  #있으면 +1 #없으면 0을받고 +1	
    return blood_dict

print(count_blood(blood))
print(count_blood2(blood))




# 3. 정사각형 만들기
def only_square_area(widths,heights):
    area = [] #넓이
    for w in widths: #너비
        for h in heights: #높이
            if w == h : #같을때는 정사각형
                area.append(w*h) #리스트로 저장
    
    return area 

def only_square_area2(widths,heights):
    area = [w*h for w in widths for h in heights if w == h] #넓이
    return area 

widths = [32,55,44,50,63]
heights= [13,44,32,40,55]

print(only_square_area(widths,heights))
print(only_square_area2(widths,heights))