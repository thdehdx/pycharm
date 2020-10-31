def solution(w,h):
    answer = 1
    full=w*h
    #최대공약수
    gcm=1
    for k in range(2,min(w,h)+1):
        while(w%k==0)&(h%k==0):
            w=w//k
            h=h//k
            gcm=gcm*k
            continue
    ###########
    trash=w+h-1
    trash*=gcm
    answer=full-trash
    return answer