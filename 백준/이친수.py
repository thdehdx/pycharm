n=int(input())
ans=[[0]*2 for _ in range(92)]
ans[1][0]=0
ans[1][1]=1

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        ans[i][0]=ans[i-1][0]+ans[i-1][1]
        ans[i][1]=ans[i-1][0]
    print(sum(ans[n]))
