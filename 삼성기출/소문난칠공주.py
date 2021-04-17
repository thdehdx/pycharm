from itertools import combinations

def bond(list_a):
    one=0
    maximum=0
    for c in list_a:
        bondCnt=0
        if c-1 in list_a and c%5!=0:
            bondCnt+=1
        if c+1 in list_a and (c+1)%5!=0:
            bondCnt+=1
        if c-5 in list_a:
            bondCnt+=1
        if c+5 in list_a:
            bondCnt+=1
        if bondCnt==0:
            break
        if maximum<bondCnt:
            maximum=bondCnt
        if bondCnt==1:
            one+=1
    if bondCnt==0:
        return 0
    if maximum>=one:
        return 1


cnt=0
dy=[-1,1,0,0]#12,6,9,3시 방향
dx=[0,0,-1,1]
raw_map_two = [list(input()) for _ in range(5)]#5*5
position=[]
result_map=[]
index_map=[]
for a in range(25):
    index_map.append(a)
for a in range(5):
    for b in range(5):
        if raw_map_two[a][b]=="S":
            position.append(a*5+b)
list_combi=list(combinations(index_map,7))

for a in list_combi:
    temp=[]
    missCnt=0
    for c in position:
        if c not in a:
            missCnt+=1
        if missCnt==2:
            break
    if missCnt==2:#S 4개이상 미포함
        continue
    flag=bond(a)
    if flag:
        result_map.append(a)

print(len(result_map))