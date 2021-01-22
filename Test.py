board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

big = len(board) if len(board) > len(board[0]) else len(board[0])
print(big)