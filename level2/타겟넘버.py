def solution(numbers, target):
    cnt = 0
    len_numbers = len(numbers)
    test=[0 for _ in range(len(numbers))]
    def operator(idx=0):
        if idx < len_numbers:
            test[idx] = numbers[idx]*1
            operator(idx+1)

            test[idx] = numbers[idx]*-1
            operator(idx+1)

        elif sum(test) == target:
            nonlocal cnt
            cnt += 1

    operator()

    return cnt