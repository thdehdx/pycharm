n=int(input())
temp=list(map(int,input().split()))
p=[0]
for a in temp:
    p.append(a)
ans=[0]*1001
if n==0 or n==1:
    print(p[n])
elif n==2:
    print(max(p[1]+p[1],p[2]))
else :
    ans[0]=p[0]
    ans[1]=p[1]
    ans[2]=max(p[1]+p[1],p[2])
    for i in range(3,n+1):
        temp=[]
        for j in range(0,i):
            temp.append(ans[j]+p[i-j])#j번째 정답 + (i-j)개 들어있는 카드팩 가격
        ans[i]=max(temp)

    print(ans[i])