from itertools import combinations

def solution(clothes):
    answer = 0
    cloth_type=[]
    cloth_name=[]
    for i in clothes:
        if i[1] not in cloth_type:
            cloth_type.append(i[1])
            cloth_name.append(0)
        cloth_name[cloth_type.index(i[1])]+=1
    for i in range(len(cloth_name)):#테스트 1을 위함 -> 모두 1인 경우
        if cloth_name[i] > 1:
            break
    if i == len(cloth_name)-1 and cloth_name[i]==1:#테스트 1을 위함 -> 모두 1인 경우
        return 2**len(cloth_name)-1
    for i in range(1,len(cloth_type)+1):
        a=list(combinations(cloth_type,i))
        for b in a:
            temp=1
            for c in b:
                temp*=cloth_name[cloth_type.index(c)]
            answer+=temp
    return answer