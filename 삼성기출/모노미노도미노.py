def move(block):
    if block[0]==1:
        for a in range(6):#green_map 배치될 위치 탐색
            if green_map[a][block[2]]!=0:
                a-=1
                break
            elif a==5:
                a+=1
        if a==6:
            a-=1
        green_map[a][block[2]]=1#green_map 배치

        for a in range(6):#blue_map 배치될 위치 탐색
            if blue_map[a][block[1]]!=0:
                a-=1
                break
            elif a==5:
                a+=1
        if a==6:
            a-=1
        blue_map[a][block[1]]=1#blue_map 배치
    elif block[0]==2:
        for a in range(6):#green_map 배치될 위치 탐색
            if green_map[a][block[2]]!=0:
                a-=1
                break
            elif green_map[a][block[2]+1]!=0:
                a-=1
                break
            elif a==5:
                a+=1
        if a==6:
            a-=1
        green_map[a][block[2]]=2#green_map 배치
        green_map[a][block[2]+1]=2

        for a in range(6):#blue_map 배치될 위치 탐색
            if blue_map[a][block[1]]==1:
                a-=1
                break
            elif a==5:
                a+=1
        if a==6:
            a-=1
        blue_map[a][block[1]]=2#blue_map 배치
        blue_map[a-1][block[1]]=2
    elif block[0]==3:
        for a in range(6):#green_map 배치될 위치 탐색
            if green_map[a][block[2]]!=0:
                a-=1
                break
            elif a==5:
                a+=1
        if a==6:
            a-=1
        green_map[a][block[2]]=3#green_map 배치
        green_map[a-1][block[2]]=3

        for a in range(6):#blue_map 배치될 위치 탐색
            if blue_map[a][block[1]]!=0:
                a-=1
                break
            elif blue_map[a][block[1]+1]!=0:
                a-=1
                break
            elif a==5:
                a+=1
        if a==6:
            a-=1
        blue_map[a][block[1]]=3#blue_map 배치
        blue_map[a][block[1]+1]=3
def green_check():
    global score
    flag=0
    for x in range(2,6):#2~5행 확인
        count=0
        for y in range(4):
            if green_map[x][y]!=0:
                count+=1
        if count==4:#행이 꽉차면 삭제
            score+=1
            flag=1
            for y in range(4):
                green_map[x][y]=0
    return flag
def blue_check():
    global score
    flag=0
    for x in range(2,6):#2~5행 확인
        count=0
        for y in range(4):
            if blue_map[x][y]!=0:
                count+=1
        if count==4:#행이 꽉차면 삭제
            score+=1
            flag=1
            for y in range(4):
                blue_map[x][y]=0
    return flag
def green_special():
    count=0
    for x in range(2):#0~1행 확인
        for y in range(4):
            if green_map[x][y]!=0:
                count+=1
                break
    for a in range(count):#행 갯수 만큼 아랫 행 삭제
        for x in reversed(range(5)):#모든 블럭 한줄씩 내리기
            for y in range(4):
                green_map[x+1][y]=green_map[x][y]
def blue_special():
    count=0
    for x in range(2):#0~1행 확인
        for y in range(4):
            if blue_map[x][y]!=0:
                count+=1
                break
    for a in range(count):#행 갯수 만큼 아랫 행 삭제
        for x in reversed(range(5)):#모든 블럭 한줄씩 내리기
            for y in range(4):
                blue_map[x+1][y]=blue_map[x][y]
def green_down():
    nox=9
    noy=9
    for x in reversed(range(5)):#4~0행#5행은 블럭을 내릴 수 없음
        for y in range(4):
            if x==nox and y==noy:
                pass
            if green_map[x][y]!=0:#down시킬 블록 발견!
                if green_map[x][y]==2:#2블록만 양옆 블록 확인
                    single=1
                    try:
                        if green_map[x][y-1]==2:
                            single=0
                            for a in range(1,6-x):
                                if green_map[x+a][y]!=0 or green_map[x+a][y-1]!=0:#아래 블록이 있다면
                                    green_map[x+a-1][y]=2
                                    green_map[x][y]=0
                                    break
                                elif x+a==5:#경계선까지 아래 블록이 없다면
                                    green_map[x+a][y]=2
                                    green_map[x][y]=0
                    except:
                        temp=1
                    try:
                        if green_map[x][y+1]==2:
                            single=0
                            nox=x
                            noy=y+1
                            for a in range(1,6-x):
                                if green_map[x+a][y]!=0 or green_map[x+a][y+1]!=0:#아래 블록이 있다면
                                    green_map[x+a-1][y]=2
                                    green_map[x][y]=0
                                    break
                                elif x+a==5:#경계선까지 아래 블록이 없다면
                                    green_map[x+a][y]=2
                                    green_map[x][y]=0
                    except:
                        temp=1
                    if single==1:
                        for a in range(1,6-x):
                            if green_map[x+a][y]!=0:#아래 블록이 있다면
                                green_map[x+a-1][y]=2
                                green_map[x][y]=0
                                break
                            elif x+a==5:#경계선까지 아래 블록이 없다면
                                green_map[x+a][y]=2
                                green_map[x][y]=0
                else:
                    for a in range(1,6-x):
                        if green_map[x+a][y]!=0:#아래 블록이 있다면
                            green_map[x+a-1][y]=green_map[x][y]
                            green_map[x][y]=0
                            break
                        elif x+a==5:#경계선까지 아래 블록이 없다면
                            green_map[x+a][y]=green_map[x][y]
                            green_map[x][y]=0
def blue_down():
    nox=9
    noy=9
    for x in reversed(range(5)):#4~0행#5행은 블럭을 내릴 수 없음
        for y in range(4):
            if x==nox and y==noy:
                pass
            if blue_map[x][y]!=0:#down시킬 블록 발견!
                if blue_map[x][y]==3:#3블록만 양옆 블록 확인
                    single=1
                    try:
                        if blue_map[x][y-1]==3:
                            single=0
                            for a in range(1,6-x):
                                if blue_map[x+a][y]!=0 or blue_map[x+a][y-1]!=0:#아래 블록이 있다면
                                    blue_map[x+a-1][y]=3
                                    blue_map[x][y]=0
                                    break
                                elif x+a==5:#경계선까지 아래 블록이 없다면
                                    blue_map[x+a][y]=3
                                    blue_map[x][y]=0
                    except:
                        temp=1
                    try:
                        if blue_map[x][y+1]==3:
                            nox=x
                            noy=y+1
                            single=0
                            for a in range(1,6-x):
                                if blue_map[x+a][y]!=0 or blue_map[x+a][y+1]!=0:#아래 블록이 있다면
                                    blue_map[x+a-1][y]=3
                                    blue_map[x][y]=0
                                    break
                                elif x+a==5:#경계선까지 아래 블록이 없다면
                                    blue_map[x+a][y]=3
                                    blue_map[x][y]=0
                    except:
                        temp=1
                    if single==1:
                        for a in range(1,6-x):
                            if blue_map[x+a][y]!=0:#아래 블록이 있다면
                                blue_map[x+a-1][y]=3
                                blue_map[x][y]=0
                                break
                            elif x+a==5:#경계선까지 아래 블록이 없다면
                                blue_map[x+a][y]=3
                                blue_map[x][y]=0
                else:
                    for a in range(1,6-x):
                        if blue_map[x+a][y]!=0:#아래 블록이 있다면
                            blue_map[x+a-1][y]=blue_map[x][y]
                            blue_map[x][y]=0
                            break
                        elif x+a==5:#경계선까지 아래 블록이 없다면
                            blue_map[x+a][y]=blue_map[x][y]
                            blue_map[x][y]=0
n=int(input())
blocks=[]
for i in range(n):
    t,x,y=map(int,input().split())
    blocks.append([t,x,y])

red_map=list([0]*4 for _ in range(4))
green_map=list([0]*4 for _ in range(6))
blue_map=list([0]*4 for _ in range(6))

score=0
for block in blocks:
    move(block)
    green_flag = green_check()#black이 사라질 경우 down함수 호출
    blue_flag = blue_check()#black이 사라질 경우 down함수 호출
    while green_flag:#down이후에 1줄 체워지는 경우가 있어서 While로 진행
        green_down()
        green_flag=green_check()
    green_special()
    while blue_flag:#down이후에 1줄 체워지는 경우가 있어서 While로 진행
        blue_down()
        blue_flag=blue_check()
    blue_special()

blockCount=0
for x in range(6):#모든 과정 후, 남은 블록 세는 과정
    for y in range(4):
        if green_map[x][y]!=0:
            blockCount+=1
        if blue_map[x][y]!=0:
            blockCount+=1
print(score)
print(blockCount)