import heapq

def solution(scoville, k):
    heap=[]
    answer = 0
    for i in scoville:
        heapq.heappush(heap,i)
    while(heap[0]<k):
        if(len(heap)==1):
            answer=-1
            break
        nNum=heapq.heappop(heap)+heapq.heappop(heap)*2
        heapq.heappush(heap,nNum)
        answer+=1
    return answer