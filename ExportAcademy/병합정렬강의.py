def merge(left,right):
    result = [] #두개의 분할된 리스트를 병합하여 result를 만듦

    while len(left)>0 and len(right)>0:#양쪽 리스트에 원소가 남아 있는 경우
        #두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)>0:#왼쪽 리스트가 원소가 남아있는 경우
        result.extend(left)
    if len(right)>0:#오른쪽 리스트에 원소가 남아있는 경우
        result.extend(right)
    return result
def merge_sort(m):
    if len(m)<=1:#사이즈가 0이거나 1인 경우, 바로 리턴
        return m
    #1. Divide 부분
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    #리스트의 크기가 1이 될때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right=merge_sort(right)

    # 2. Conquer부분: 분할된 리스트들 병합
    return merge(left,right)