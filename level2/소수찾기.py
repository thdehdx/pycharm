from itertools import permutations
from math import sqrt

def solution(numbers):
    answer = 0
    rawNum=[]
    numlist=list(numbers)
    for c in range(1,len(numlist)+1):
        numAll=list(permutations(numlist,c))
        for a in numAll:
            temp=""
            for b in range(c):
                temp+=a[b]
            if int(temp) not in rawNum:
                rawNum.append(int(temp))
    for a in rawNum:
        if a==2 or a==3 :
            answer+=1
            continue
        for b in range(2,int(sqrt(a))+1):
            if a%b==0 and a!=b:
                break
            elif b==int(sqrt(a)):
                answer+=1
    return answer

solution("13")