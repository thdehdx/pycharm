import sys
import copy
from itertools import combinations
from collections import deque

def dfs(q,moveCnt):
    global ans
    #print(q)
    nq=deque()
    nMoveCnt=moveCnt+1
    while(len(q)>0):
        temp=q.popleft()
        y=temp[0]
        x=temp[1]
        for dir in range(4):
            ny=y+dy[dir]
            nx=x+dx[dir]
            if not(0<=ny<n and 0<=nx<n):#범위 벗어났을 경우
                continue
            if raw_map[ny][nx]==0 and moveMap[ny][nx]==-1:#바이러스를 넣을 수 있다면 and 바이러스가 지나간적 없는 경우
                moveMap[ny][nx]=nMoveCnt
                nq.append([ny,nx])
            elif raw_map[ny][nx]==1:#벽일 경우
                moveMap[ny][nx]="-"
    if len(nq)>0:
        dfs(nq,nMoveCnt)
    else:
        for i in range(n):
            for j in range(n):
                if moveMap[i][j]==-1 and raw_map[i][j]==0:#빈칸에 바이러스를 모든 맵에 못퍼트린 경우
                    return 0#ans업데이트 금지
        if ans>moveCnt:
            ans=moveCnt
    return 0

n, m = map(int, input().split())
raw_map = [list(map(int, input().split())) for _ in range(n)]  # N*N

dy = [-1, 1, 0, 0]  # 12,6,9,3시 방향
dx = [0, 0, -1, 1]

v = []  # virus 좌표

for a in range(n):  # map검사
    for b in range(n):
        if raw_map[a][b] == 2:  # 해당 좌표에 바이러스를 놓을 수 있을 경우
            v.append([a, b])
            raw_map[a][b]=0 #빈칸으로 생성#맵에 0(빈공간)과 1(벽)만남음

combi = list(combinations(v, m))

#print(combi)

ans = sys.maxsize
for a in combi:#a:좌표3개 모음
    q=deque()#큐생성
    moveCnt=0
    moveMap = [[-1] * n for _ in range(n)]#1개 combi마다 바이러스 움직임을 담을 n*n의 새로운 맵 생성
    #copy_raw_map=copy.deepcopy(raw_map)
    #print(a)
    for b in a:#b : 좌표1개씩 분리
        q.append(b)
        moveMap[b[0]][b[1]]=moveCnt#moveMap에 0입력
    #print(moveMap)
    dfs(q,moveCnt)
    #print(moveMap)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)


