def turn(num,direction):
    global topni
    if direction==1:
        temp=topni[num][7]
        for i in reversed(range(7)):
            topni[num][i+1]=topni[num][i]
        topni[num][0]=temp
    elif direction==-1:
        temp=topni[num][0]
        for i in range(7):
            topni[num][i]=topni[num][i+1]
        topni[num][7]=temp

topni=[0]*4#4개 톱니바퀴
for i in range(4):
    topni[i]=list(input())#N극=0, S극=1, 오른쪽접촉인덱스=2, 왼쪽접촉인덱스=6,
k=int(input())
ks=[]
for i in range(k):#1:시계방향, -1:반시계방향
    num, direction=map(int,input().split())
    ks.append([num-1,direction])



for j in ks:
    turns=[]
    num, direction=j[0], j[1]
    turns.append([num,direction])#본인은 무조건 회전
    num_temp=num
    direction_temp=direction
    while(num_temp>0):#왼쪽으로 검사
        if topni[num_temp][6]!=topni[num_temp-1][2]:#왼쪽 톱니와 극성이 다르면
            num_temp-=1
            direction_temp*=(-1)
            turns.append([num_temp,direction_temp])#왼쪽 톱니는 반대방향으로 turn
        else:
            break
    num_temp=num
    direction_temp=direction
    while(num_temp<3):#오른쪽으로 검사
        if topni[num_temp][2]!=topni[num_temp+1][6]:#오른쪽 톱니와 극성이 다르면
            num_temp+=1
            direction_temp*=(-1)
            turns.append([num_temp,direction_temp])#오른 톱니는 반대방향으로 turn
        else:
            break
    for t in turns:#돌릴 톱니들
        turn(t[0],t[1])#t[0]: 톱니번호 t[1]: 방향
answer=0
for i in range(len(topni)):
    if topni[i][0]=="1":
        if i==0:
            answer+=1
        elif i==1:
            answer+=2
        elif i==2:
            answer+=4
        elif i==3:
            answer+=8
print(answer)