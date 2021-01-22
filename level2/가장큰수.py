def solution(numbers):
    answer = ''
    three=[]
    for a in numbers:
        if len(str(a))!=3:
            b=str(a)
            while len(b)!=3:
                b+=b[0]
            three.append(int(b))
        else:
            three.append(a)
    while len(three)>1:
        numMax=three.index(max(three))
        answer+=str(numbers[numMax])
        del numbers[numMax]
        del three[numMax]
    answer+=str(numbers[0])
    return answer

solution([6,10,2])