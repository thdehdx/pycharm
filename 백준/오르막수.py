n=int(input())
ans=[[0]*10 for _ in range(1002)]
for j in range(10):
    ans[1][j]=1

if n==0:
    print(0)
elif n==1:
    print(10)
else:
    for i in range(2,n+1):
        for j in range(10):
            for k in range(j+1):
                ans[i][j]+=ans[i-1][k]
    print(sum(ans[n])%10007)
