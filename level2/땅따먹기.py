def solution(land):
    answer = 0
    #위에서 아래로
    for i in range(len(land)):
        if i<len(land)-1:
            mine = [[land[i][1], land[i][2], land[i][3]], [land[i][0], land[i][2], land[i][3]],
                    [land[i][0], land[i][1], land[i][3]], [land[i][0], land[i][1], land[i][2]]]
            for a in range(4):
                land[i+1][a]+=max(mine[a])
        else:
            answer=max(land[i])
    return answer

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])