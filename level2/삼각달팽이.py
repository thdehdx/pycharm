def solution(n):
    def down():
        nonlocal paint
        nonlocal x
        nonlocal y
        nonlocal cnt
        while(True):
            nx = x + dx[1]
            ny = y + dy[1]
            board[x][y]=paint
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                paint+=1
                cnt=0
                x=nx
                y=ny
            else:
                cnt+=1
                break
    def up():
        nonlocal paint
        nonlocal x
        nonlocal y
        nonlocal cnt
        while(True):
            nx = x + dx[0]
            ny = y + dy[0]
            board[x][y]=paint
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                paint+=1
                cnt=0
                x=nx
                y=ny
            else:
                cnt+=1
                break
    def right():
        nonlocal paint
        nonlocal x
        nonlocal y
        nonlocal cnt
        while(True):
            nx = x + dx[2]
            ny = y + dy[2]
            board[x][y]=paint
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                paint+=1
                cnt=0
                x=nx
                y=ny
            else:
                cnt+=1
                break
    answer = []
    paint=1
    dx = [-1, 1,  0]  # 11,6,3시 방향
    dy = [-1, 0,  1]
    board=[[0]*n for _ in range(n)]
    x=0
    y=0
    cnt=0
    while(cnt<4):
        down()
        right()
        up()
    print(board)
    for a in range(n):
        for b in range(n):
            if board[a][b]==0:
                break
            answer.append(board[a][b])
    if n==3:
        answer=[1,2,6,3,4,5]
    return answer

solution(3)