import sys

def dfs(idx):
    global answer
    if sum(team) == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if team[i] and team[j]:
                    start += raw_map[i][j]
                elif not team[i] and not team[j]:
                    link += raw_map[i][j]
        answer = min(answer, abs(start - link))
    for i in range(idx, n):
        team[i] = 1
        print(team)
        if sum(team)<((n//2)+1):
            dfs(i + 1)
        team[i] = 0

n=int(input())
raw_map = [list(map(int,input().split())) for _ in range(n)]#N*N

team = [0 for _ in range(n)]
answer = sys.maxsize
dfs(0)
print(answer)