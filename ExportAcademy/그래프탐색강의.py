#DFS
#G:그래프, v:시작 정점
#visited:정점의 방문 정보 표시, False로 초기화
#G[v]:그래프 G에서 v의 인접 정점 리스트

def DFS_Recursive(G,v):
    visited[v]=True
    visit[v]
    for w in G[v]:
        if not visited[w]:
            DEF_Recursive(G,w)

#G:그래프, S: 스택, v: 시작 정점
#visited : 정점의 방문 정보 표시, False로 초기화
#G[v]:그래프 G에서 v의 인접 정점 집합

def DFS_Iterative(S,v):
    S=[v]
    while stack:
        v=S.pop()
        if v not in visited:
            visited.append(v)
            visit()
            S.extend(G[v]-set(visited))
        return visited

#G:그래프 , Q:큐, v=시작 정점
#visited:정점의 방문 정보표시, False로 초기화
# G[v]: 그래프 G에서 v의 인접 정점 리스트
def BFS(Q,v):
    Q.append(v)
    visited[v]=True
    visit(v)
    while Q:
        v=Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w]=True
                visit(w)