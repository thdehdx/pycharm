def cube(side,dir):
    global u,f,d,b,l,r
    if side=="u":
        side_map=u
        one=[l,b,r,f]#왼,위,오,아
    elif side=="f":
        side_map=f
        one=[l,u,r,d]#왼,위,오,아
    elif side=="d":
        side_map=d
        one=[r,b,l,f]#왼,위,오,아
    elif side=="b":
        side_map=b
        one=[r,u,l,d]#왼,위,오,아
    elif side=="l":
        side_map=l
        one=[b,u,f,d]#왼,위,오,아
    elif side=="r":
        side_map=r
        one=[f,u,b,d]#왼,위,오,아
    side_map=turn(side_map,dir)
    move(one,side,dir)
def turn(side_map,dir):
    N = len(side_map)
    ret = [[0] * N for _ in range(N)]
    if dir =="+":
        for x in range(N):
            for y in range(N):
                ret[y][N-1-x] = side_map[x][y]
    else:
        for x in range(N):
            for y in range(N):
                ret[N - 1 - y][x] = side_map[x][y]
    return ret
def move(one,side,dir):
    global u,f,d,b,l,r
    if side=="u":
        line=[[[0,0],[0,1],[0,2]],[[0,0],[0,1],[0,2]],[[0,0],[0,1],[0,2]],[[0,0],[0,1],[0,2]]]#왼,위,오,아
    elif side=="f":
        line=[[[0,2],[1,2],[2,2]],[[2,2],[2,1],[2,0]],[[2,0],[1,0],[0,0]],[[2,2],[2,1],[2,0]]]#왼,위,오,아
    elif side=="d":
        line=[[[2,0],[2,1],[2,2]],[[2,0],[2,1],[2,2]],[[2,0],[2,1],[2,2]],[[2,0],[2,1],[2,2]]]#왼,위,오,아
    elif side=="b":
        line=[[[0,2],[1,2],[2,2]],[[0,0],[0,1],[0,2]],[[2,0],[1,0],[0,0]],[[0,0],[0,1],[0,2]]]#왼,위,오,아
    elif side=="l":
        line=[[[0,2],[1,2],[2,2]],[[0,0],[1,0],[2,0]],[[2,0],[1,0],[0,0]],[[2,2],[1,2],[0,2]]]#왼,위,오,아
    elif side=="r":
        line=[[[0,2],[1,2],[2,2]],[[0,2],[1,2],[2,2]],[[2,0],[1,0],[0,0]],[[2,0],[1,0],[0,0]]]#왼,위,오,아
    if dir =="+":
        for h in range(3):
            temp=one[2][line[2][h][0]][line[2][h][1]]
            for g in range(2):
                one[g+1][line[g+1][h][0]][line[g+1][h][1]]=one[g][line[g][h][0]][line[g][h][1]]
            one[0][line[0][h][0]][line[0][h][1]]=temp
    else:
        for h in range(3):
            temp=one[0][line[0][h][0]][line[0][h][1]]
            for g in range(1,3):
                one[g-1][line[g-1][h][0]][line[g-1][h][1]]=one[g][line[g][h][0]][line[g][h][1]]
            one[2][line[2][h][0]][line[2][h][1]]=temp

test_case=int(input())
for a in range(test_case):
    turn_cnt=input()
    turn_map=list(map(str,input().split()))
    u=[["w"]*3 for _ in range(3)]#맵 매번 초기화
    f=[["r"]*3 for _ in range(3)]
    d=[["y"]*3 for _ in range(3)]
    b=[["o"]*3 for _ in range(3)]
    l=[["g"]*3 for _ in range(3)]
    r=[["b"]*3 for _ in range(3)]
    for c in turn_map:
        side, dir = list(c) #면과 방향 분리 저장
        side=side.lower()
        cube(side,dir)#큐브 회전 작업
        print("A")
        print(u)
        print(f)
        print(l)
        print(r)
        print(b)
        print(d)
    for s in u:
        print(''.join(s))
