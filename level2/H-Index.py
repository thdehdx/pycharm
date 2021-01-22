def solution(citations):
    answer = 0
    citations.sort(reverse=True)#내림차순
    cnt=0
    for a in citations:
        cnt+=1
        if a<cnt:#업데이트 필요없을시 break
            break
        else:#a만큼 인용된 논문이 a편 이상 될때까지 업데이트
            answer=cnt
    return answer