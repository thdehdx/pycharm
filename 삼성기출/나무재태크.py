def spring():
    for x in range(n):
        for y in range(n):
            tree_map[x][y].sort()#나무 나이순 오름차순 정렬
            for a in range(len(tree_map[x][y])):#어린 나무부터 양분 주기
                if raw_map[x][y]>=tree_map[x][y][a]:#먹을 양분이 충분하다면
                    raw_map[x][y]-=tree_map[x][y][a]#양분 먹이기
                    tree_map[x][y][a]+=1#양분먹은 나무 나이 +1
                else:#먹을 양분이 충분하지 않다면
                    for b in range(a,len(tree_map[x][y])):#"각각"의 나무를 //2해야해서 sum()사용 x
                        raw_map[x][y]+=tree_map[x][y][b]//2#summer
                    tree_map[x][y]=tree_map[x][y][0:a]#a번째 나무부터 끝까지 모두 양분이 없어서 죽음
                    break
            for a in range(len(tree_map[x][y])):#양분 공급 완료된 좌표->fall 준비
                if tree_map[x][y][a]%5==0:
                    five.append([x,y])#5의 배수 나무가 있는 좌표 저장, 여러번 추가될 수도 있음
def fall():
    for a in five:#5의 배수의 나이를 가진 나무가 존재하는 좌표
        for b in range(8):#인접한 8칸
            nx=a[0]+nearx[b]
            ny=a[1]+neary[b]
            if 0<=nx<n and 0<=ny<n:#땅 안에 있을 경우
                tree_map[nx][ny].append(1)#1살 나무 추가

def winter(year):#양분 주기#마지막 년도일 경우 남은 나무 cnt역할
    global cnt
    for x in range(n):
        for y in range(n):
            raw_map[x][y]+=plus_map[x][y]
            if year==k-1:#마지막 년도일 경우 남은 나무 cnt
                cnt+=len(tree_map[x][y])

n,m,k=map(int,input().split())
raw_map = [[5]*n for _ in range(n)]#N*N
tree_map = [[[] for _ in range(n)] for _ in range(n)]#N*N
plus_map = [list(map(int,input().split())) for _ in range(n)]#N*N
tree_info = [list(map(int,input().split())) for _ in range(m)]#m*3
nearx=[-1,-1,-1,0,0,1,1,1]#인접한 8칸
neary=[-1,0,1,-1,1,-1,0,1]#인접한 8칸
cnt=0
for a in range(m):#x,y좌표 -1씩 진행
    for b in range(2):
        tree_info[a][b]-=1
    tree_map[tree_info[a][0]][tree_info[a][1]].append(tree_info[a][2])
for year in range(k):
    five=[]
    spring()
    fall()
    winter(year)
print(cnt)