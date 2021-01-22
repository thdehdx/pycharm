def solution(brown, yellow):
    answer = []
    yak=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            yak.append(i)
    if len(yak)%2==0:#약수 갯수가 짝수
        gil=len(yak)//2
    else:
        gil=(len(yak)+1)//2
    for i in range(gil):
        if (yak[len(yak)-1-i]+2)+yak[i]==(brown//2):
            break
    answer.append(yak[len(yak)-1-i]+2)
    answer.append(yak[i]+2)
    return answer