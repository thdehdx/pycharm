import copy

def move(y,x,movedCnt,dir,percent):
    global totalPercent
    movedCnt+=1
    percent = percent * raw[dir]/100
    copy_raw_map[y][x]=1
    #print(copy_raw_map)
    #print(raw[dir])
    #print(percent)
    if movedCnt==n:
        #print("end")
        copy_raw_map[y][x]=0
        totalPercent+=percent
        return 0
    for b in range(1,5):
        ny=y+dy[b]
        nx=x+dx[b]
        #print(ny)
        #print(nx)
        if 0<=ny<(1+n*2) and 0<=nx<(1+n*2) and raw_map[ny][nx]==0:
            move(ny,nx,movedCnt,b,percent)
    copy_raw_map[y][x]=0

dy=[0,0,0,1,-1]#3,9,6,12시 방향
dx=[0,1,-1,0,0]
raw=list(map(int,input().split()))#n#3동E#9서W#6남S#12북N
n=raw[0]
raw_map=[[0]*(1+n*2) for _ in range((1+n*2))]#(1+n*2)*(1+n*2)
raw_map[n][n]=1
copy_raw_map=copy.deepcopy(raw_map)

totalPercent=0
for a in range(1,5):
    movedCnt=0
    ny=n+dy[a]
    nx=n+dx[a]
    percent = 1
    move(ny,nx,movedCnt,a,percent)
print(totalPercent)