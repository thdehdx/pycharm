def calc(l):
    global ans
    ans+=1
    nl=[]
    for a in l:
        nl.append(a-1)
        if a%3==0 and a>=3:
            nl.append(a/3)
        if a%2==0 and a>=2:
            nl.append(a/2)
    return nl

n=int(input())
l=[]
l.append(n)
ans=0
if n==1:
    print(ans)
else:
    while(1):
        l=calc(l)
        if min(l)==1:
            break
    print(ans)