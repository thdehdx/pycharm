def solution(phone_book):
    answer = True
    for a in range(len(phone_book)-1):
        for b in range(a+1,len(phone_book)):
            if len(phone_book[a])>len(phone_book[b]):
                short=len(phone_book[b])
            else:
                short=len(phone_book[a])
            if phone_book[a][:short]==phone_book[b][:short]:
                return False
    return answer

print(solution(["111113","1112","12"]))