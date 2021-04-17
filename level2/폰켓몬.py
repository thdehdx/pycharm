def solution(nums):
    maximum=len(nums)/2
    my_set = set(nums) #집합set으로 변환
    nums = list(my_set) #list로 변환
    if len(nums)<maximum:
        return len(nums)
    else:
        return maximum