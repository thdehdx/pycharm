def solution(priorities, location):
    answer = 0
    exist=[]#priorities에 있는 숫자들 곂치지않게
    isEnd=False
    for i in priorities:
        if i not in exist:
            exist.append(i)
    exist.sort(reverse=True)#[9,1]
    nowMaxIdx=0
    cnt=len(priorities)
    while(isEnd==False):
        for i in range(len(priorities)):
            first=priorities.pop(0)
            if first<exist[nowMaxIdx]:
                priorities.append(first)
                cnt-=1
                if cnt == 0:
                    nowMaxIdx+=1
            else:
                answer+=1
                cnt=len(priorities)
                if location==0:
                    isEnd=True
                    break
            if location==0:
                location=len(priorities)
            location-=1
    return answer

solution([1, 1, 9, 1, 1, 1],0)