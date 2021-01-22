from itertools import combinations
from operator import itemgetter
import copy

def sadari(start,x,y):#사다리 게임
    global temp_sadari_map
    global sum
    if y==h-1:#맨 아래 도착
        if temp_sadari_map[y][x] == 1:#맨 아래 선이 있을 경우 마지막 좌우 이동
            x+=1
        elif temp_sadari_map[y][x]==-1:#맨 아래 선이 있을 경우 마지막 좌우 이동
            x-=1
        if start==x:#같은 자리 도착검사
            sum+=1
            return 1
        return 0
    if temp_sadari_map[y][x]==0:
        return sadari(start,x,y+1)
    elif temp_sadari_map[y][x]==1:
        return sadari(start,x+1,y+1)
    elif temp_sadari_map[y][x]==-1:
        return sadari(start,x-1,y+1)

def combi():#선 그을 수 있는 경우의 수 저장
    global line_combi
    for i in line_list:#1개 조합#따로 조합 없이 저장
        line_combi.append([i])
    for i in range(2,4):#2,3개 조합
        temp=list(combinations(line_list,i))
        for j in temp:
            for k in range(len(j)-1):
                if j[k][0]==j[k+1][0] and abs(j[k][1]-j[k+1][1])==1:
                    break
                else:
                    if k==len(j)-2:#마지막 검사까지 break안되었을 경우
                        line_combi.append(j)

def same_try():#조합 실제로 시도하며 확인
    global temp_sadari_map
    global sum
    global length
    for i in line_combi:
        sum=0
        temp_sadari_map=copy.deepcopy(sadari_map)
        for j in i:#사다리 맵에 가로 선 그리기 작업
            temp_sadari_map[j[0]][j[1]]=1
            temp_sadari_map[j[0]][j[1]+1]=-1
        for k in range(n):#사다리게임 진행
            start=k
            if sadari(start,k,0)==0:
                break
        if sum==n:#n개 모두 제자리로 도착 했다면
            length=len(i)#그은 선 갯수
            return 1
    return 0#모든 경우의 수 모두 시도 했으나 실패할 경우

n,m,h=map(int,input().split())
sadari_map=[[0]*n for _ in range(h)]#n*h
line_list=[]
line_combi=[]
temp_sadari_map=[]
sum=0
length=0
for i in range(m):
    a,b=map(int,input().split())
    a= a-1#index화
    b= b-1#index화
    sadari_map[a][b]=1
    sadari_map[a][b+1]=-1
for i in range(n-1):#선을 그을 수 있는 좌표를 가진 list 작성
    for j in range(h):
        if sadari_map[j][i]==0 and sadari_map[j][i+1]==0:#선 그을 자리 왼/오 에 선이 없는지 확인
            line_list.append([j,i])
line_list.sort(key=itemgetter(0))
combi()
if same_try():
    print(length)
else:
    print("-1")