def solution(progresses, speeds):
    num=[]
    answer = []
    for i in range(len(progresses)):
        num.append(i)
    while(len(num)>0):
        for i in num:
            progresses[i]+=speeds[i]

        cnt=0
        if progresses[0]>=100:
            while(progresses[0]>=100):
                cnt+=1
                del progresses[0]
                del speeds[0]
                del num[-1]
                if len(progresses)==0:
                    break
        if cnt>0:
            answer.append(cnt)
    return answer

solution([93, 30, 55],[1, 30, 5])