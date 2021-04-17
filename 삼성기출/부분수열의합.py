from itertools import combinations

n=int(input())
s=list(map(int,input().split()))
combi=[]
sum=[]

if 1 not in s:
    print(1)
else:
    for idx in range(len(s)):#2개이상 합구하기에 사용
        combi.append(idx)

    for a in s:#단일 합저장
        if a not in sum:
            sum.append(a)

    for k in range(2,len(s)+1):#2개이상 합구하기
        list_combi=combinations(combi,k)

        for a in list_combi:
            addResult = 0
            for b in a:
                addResult+=s[b]
            if addResult not in sum:
                sum.append(addResult)
    sum.sort()

    for a in range(len(sum)):
        if a+1 !=sum[a]:
            print(a+1)
            break
        elif a+1 == len(sum):
            print(a+2)
