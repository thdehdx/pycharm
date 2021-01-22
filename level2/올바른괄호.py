def solution(s):
    list_s=s
    cnt=0
    answer = True
    for a in range(len(list_s)):
        if list_s[a]=="(":
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                return False
    if cnt!=0:
        return False
    return True