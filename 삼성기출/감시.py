def checkmap(map,i):
    for j in range(dir[i]):
        for k in j:
            return


def cctv(map):
    for i in reversed(range(5)):
        for j in position[i]:
            if i==4:
                for k in range(j[1]+1,m):
                    if map[j[0]][k]==6:
                        break
                    else:
                        map[j[0]][k]="#"
                for k in range(j[1]-1,-1,-1):
                    if map[j[0]][k]==6:
                        break
                    else:
                        map[j[0]][k]="#"
                for k in range(j[0]+1,n):
                    if map[k][j[1]]==6:
                        break
                    else:
                        map[k][j[1]]="#"
                for k in range(j[0]-1,-1,-1):
                    if map[k][j[1]]==6:
                        break
                    else:
                        map[k][j[1]]="#"

    print(map)


n,m=map(int,input().split())
raw_map = [list(map(int,input().split())) for _ in range(n)]#n*m
dir=[[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]]]#cctv별 가능한 방향 수
dx=[-1,1,0,0]#12,6,9,3시 방향
dy=[0,0,-1,1]

position = [[], [], [], [], [],[]]
for a in range(n):
    for b in range(m):
        if 0 < raw_map[a][b] <= 6:
            position[raw_map[a][b] - 1].append([a, b])  # cctv,벽 좌표저장
print(position)
cctv(raw_map)