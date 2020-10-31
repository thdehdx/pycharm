import copy
def rotate_90():
    global raw_map
    ret = [[0] * square for _ in range(square)]
    for c in range(square):
        for d in range(square):
            ret[d][square-1-c] = raw_map[c+startPoint[0]][d+startPoint[1]]
    for c in range(square):
        for d in range(square):
            raw_map[c+startPoint[0]][d+startPoint[1]]=ret[c][d]#raw_map업데이트 완료

def melt(map,a):
    global result_sum
    sum_go = False
    if a == q-1:#마지막 후일 경우 sum진행
        sum_go = True
    for c in range(row):
        for d in range(row):
            if raw_map[c][d]==0:
                continue
            if sum_go:
                result_sum+=raw_map[c][d]
            cnt=0
            for e in range(4):
                nx=c+dx[e]
                ny=d+dy[e]
                if 0<=nx<row and 0<=ny<row:
                    if raw_map[nx][ny]==0:
                        cnt+=1
                else:
                    cnt+=1
                if cnt==2:
                    map[c][d]-=1
                    if sum_go:
                        result_sum-=1
                    break
    return map

def map_big(x,y):
    global raw_map
    global temp_cnt
    global big_cnt
    raw_map[x][y]=0
    temp_cnt+=1
    for e in range(4):
        nx=x+dx[e]
        ny=y+dy[e]
        if 0<=nx<row and 0<=ny<row:
            if raw_map[nx][ny]>0:
                map_big(nx,ny)

n,q=map(int,input().split())
row=2**n#2^n의 raw_map 만들 준비
raw_map=[list(map(int,input().split()))for _ in range(row)]#2^n*2^n
l=list(map(int,input().split()))
dx=[-1,1,0,0]#12,6,9,3시 방향
dy=[0,0,-1,1]
big_cnt=0#가장 큰 덩어리가 차지하는 칸의 개수
temp_cnt=0#big_cnt와 비교할 변수
result_sum=0
for a in range(q):#q번 마법시전
    startPoint=[0,0]#격자의 (0,0)좌표
    square=2**l[a]#2^l의 격자 단위
    startPoint[1]-=square#아래 for문 첫 좌표를 [0,0]으로 하기 위한 작업
    if l[a]!=0:
        for b in range(int(row/square)**2):#격자단위 갯수만큼 반복#격자[0,0]에 들어갈raw_map좌표탐색
            if startPoint[1] + square<row:#map(가로)을 안 벗어날 경우
                startPoint[1] += square
            else:#map(가로)을 벗어날 경우
                startPoint[0] += square
                startPoint[1] = 0
            rotate_90()#90도 회전
    melt_map=copy.deepcopy(raw_map)#melt 결과물로 쓰일 map
    raw_map=melt(melt_map,a)
print(result_sum)
for c in range(row):
    for d in range(row):
        if temp_cnt!=0 and temp_cnt>big_cnt:
            big_cnt=temp_cnt
        if raw_map[c][d]!=0:
            temp_cnt=0
            result_big=map_big(c,d)#q번 시전 후 남아있는 얼음중 가장 큰 덩어리
print(big_cnt)