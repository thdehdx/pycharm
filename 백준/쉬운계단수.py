n=int(input())
temp=[[0]*10 for _ in range(102)]
for j in range(1,10):
    temp[1][j]=1
temp[1][0]=0
if n==0:
    print(0)
elif n==1:
    print(9)
else :
    for i in range(2,n+1):
        for j in range(1,9):
            temp[i][j]=temp[i-1][j-1]+temp[i-1][j+1]
        temp[i][0]=temp[i-1][1]
        temp[i][9]=temp[i-1][8]
    print(sum(temp[n]) % 1000000000)