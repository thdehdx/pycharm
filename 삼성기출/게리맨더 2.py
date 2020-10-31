import sys

def sum(point):
    x=point[0]
    y=point[1]
    d1=point[2]
    d2=point[3]
    sum=[0]*5
    for a in range(d1+1):
        for b in range(d2+1):
            group_map[x+a][y-a]=5
            group_map[x+b][y+b]=5
            group_map[x+d1+b][y-d1+b]=5
            group_map[x+d2+a][y+d2-a]=5
    for a in range(n):
        exist=[]
        for b in range(n):
            if group_map[a][b]==5:
                exist.append(b)
        if len(exist)>1:
            for b in range(min(exist),max(exist)+1):
                group_map[a][b]=5
    for r in range(n):
        for c in range(n):
            if group_map[r][c]==5:
                sum[4]+=raw_map[r][c]
            elif 0<=r<x+d1 and 0<=c<=y:
                sum[0]+=raw_map[r][c]
                group_map[r][c]=1
            elif 0<=r<=x+d2 and y<c<=n-1:
                sum[1]+=raw_map[r][c]
                group_map[r][c]=2
            elif x+d1<=r<=n-1 and 0<=c<y-d1+d2:
                sum[2]+=raw_map[r][c]
                group_map[r][c]=3
            elif x+d2<r<=n-1 and y-d1+d2<=c<=n-1:
                sum[3]+=raw_map[r][c]
                group_map[r][c]=4
            else:
                sum[4]+=raw_map[r][c]
                group_map[r][c]=5
    return max(sum)-min(sum)

n=int(input())
raw_map = [list(map(int,input().split())) for _ in range(n)]#N*N
point=[]#[x,y,d1,d2]
x=[]
y=[]
d1=[]
d2=[]
result=sys.maxsize
for i in range(n):
    x.append(i)
    y.append(i)
for i in range(1,n+1):
    d1.append(i)
    d2.append(i)
for a in x:
    for b in y:
        for c in d1:
            for d in d2:
                if a+c+d<n and 0<b-c<b+d<n:
                    point.append([a,b,c,d])
                else:
                    break

for i in point:
    group_map = [[0]*n for _ in range(n)]#N*N
    temp=sum(i)
    if result>temp:
        result=temp
print(result)


