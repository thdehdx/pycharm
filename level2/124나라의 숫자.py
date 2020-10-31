from collections import deque
def solution(n):
    answer, prs = "", deque([])
    while n > 0 :
        prs.append('412'[n%3])

        if n % 3 == 0:
            n //=3
            n -= 1
        else:
            n //= 3
        answer += prs.popleft()

    return answer[::-1]

print(solution(34))