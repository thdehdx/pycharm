#a: 검색할 리스트
#key: 검색하고자 하는 값

def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = start + (end - start)//2
        if key == a[middle]:#검색 성공
            return middle
        elif key < a[middle]:
            end = middle -1
        else :#a[middle]<key:
            start=middle+1
    return -1#검색실패