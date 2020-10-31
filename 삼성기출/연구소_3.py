import sys
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
raw_map = [list(map(int, input().split())) for _ in range(n)]  # N*N

dy = [-1, 1, 0, 0]  # 12,6,9,3시 방향
dx = [0, 0, -1, 1]

v = []  # virus 좌표

for a in range(n):  # map검사
    for b in range(n):
        if raw_map[a][b] == 2:  # 해당 좌표에 바이러스가 있을 경우
            v.append([a, b])

combi = list(combinations(v, m))

ans = sys.maxsize
for i in range(len(combi)):
    q, q2 = deque(), deque()
    c = [[-1] * n for _ in range(n)]
    for j in range(m):
        c[combi[i][j][0]][combi[i][j][1]] = 0
        q.append([combi[i][j][0], combi[i][j][1]])
    print(q)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)


