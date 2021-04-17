from itertools import combinations
import copy

def detect(combi):
    global resultCnt
    if resultCnt>=CanMax:
        return 1
    copy_possible_word=copy.deepcopy(possible_word)
    cnt=0
    for word in copy_possible_word:#최대로 배울수 있는 단어 갯수 검사
        flag=0
        for c in combi:
            if c in word:
                flag+=1
        if len(word)==flag+5:
            cnt+=1
    if resultCnt<cnt:
        resultCnt=cnt
    return 0

resultCnt=0
CanMax=0
n,k=map(int,input().split())#n 남극총단어갯수 1이상~50이하 ... k 가르칠수 있는 최대 글자갯수 0이상~26이하
#영어 소문자, 길이 8이상~15미만
raw_map = [list(input()) for _ in range(n)]

learned=["a","n","t","i","c"]
plus_learn=[]#추가로 배워야할 글자
possible_word=[]#배울 가능성이 있는 단어들

if k<5:#고정 단어도 못배울 경우 end
    print(0)
else:
    #k-=5#고정 단어 갯수 제거
    for word in raw_map:

        set_word=set(word)#중복제거
        list_word=list(set_word)#중복제거

        if len(list_word)>k:#추가로 배워야할 글자가 k개보다 많으면 pass
            continue
        else:
            #for learned_word in learned:#5개 고정 제거#["a","n","t","i","c"]
                #list_word.remove(learned_word)
            possible_word.append(list_word)#배울 수 있는 가능성이 있는 단어들에 추가

        for plus in list_word:
            if plus not in plus_learn:# 추가로 배워야할 글자 집합에 미존재할 경우
                plus_learn.append(plus)

    for learned_word in learned:#5개 고정 제거#["a","n","t","i","c"]
        plus_learn.remove(learned_word)
    list_combi = list(combinations(plus_learn, k-5))#조합
    for word in possible_word:
        if CanMax<k-5+len(word)-6:
            CanMax=k-5+len(word)-6


    for combi in list_combi:
        flag=detect(combi)
        if flag==1:
            break

    print(resultCnt)


