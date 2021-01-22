#a:리스트, l:시작 인덱스, r=끝 인덱스
def quickSort(a,l,r):
    if l<r:
        s=partition(a,l,r)#pivot위치 반환
        quickSort(a,l,s-1)
        quickSort(a,s+1,r)
#Hoare-Partition 알고리즘(호어 파티션 알고리즘)
def partition(a,l,r):
    p=a[l]
    i= l+1
    j = r
    while i <= j:
        while(i<=j and a[i]<=p): i+=1
        while(i<=j and a[j]>=p): j-=1
        if i<=j:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j