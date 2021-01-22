def solution(board):
    answer=0
    num=[]
    for a in range(1,len(board[0])):
        for b in range(1,len(board)):
            if board[b][a]==0 or board[b-1][a]==0 or board[b][a-1]==0 or board[b-1][a-1]==0:
                continue
            num.append(board[b-1][a])
            num.append(board[b][a-1])
            num.append(board[b-1][a-1])
            mini=min(num)
            if answer<mini+1:
                answer=mini+1
            board[b][a]=mini+1
            num=[]
    if answer==0:
        for a in range(len(board[0])):
            if board[0][a]==1:
                return 1
        for b in range(len(board)):
            if board[b][0]==1:
                return 1

    print(board)
    return answer*answer

print(solution([[1,0],[0,0]]))