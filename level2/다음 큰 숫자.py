def solution(n):
    bn_cnt=list(format(n,"b")).count("1")
    while(True):
        n+=1
        print(list(format(n,"b")).count("1"))
        if list(format(n,"b")).count("1")==bn_cnt:
            answer=n
            break
    return answer

solution(78)