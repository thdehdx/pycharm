from collections import deque

def solution(number, k):
    dq=deque(number)
    answer = ''
    result=[]
    while(k>0 and len(dq)>0):
        result.append(dq.popleft())
        if len(result)>1:
            if result[-1]>result[-2]:
                big=result[-1]
                for a in reversed(range(len(result)-1)):
                    if result[a]<big:
                        del result[a]
                        k-=1
                        if k==0:
                            break
                    else:
                        break
        if k==0:
            while(len(dq)>0):        
                result.append(dq.popleft())
    while(k>0):
        del result[-1]
        k-=1
    answer="".join(result)
    return answer