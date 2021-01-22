def solution(s):
    answer = []
    depart=[]
    word_temp=[]
    temp=[]
    for a in s:
        if a!="," and a!="{" and a!="}":#숫자만 추출
            word_temp.append(a)
        elif a=="," and len(word_temp)>=1:#20,11이 ["2","0",",","1","1"]로 분리 되어 있음
            word="".join(word_temp)#word_temp 리스트 와 word 스트링을 통해 병합진행
            word_temp=[]#["20","11"]
            temp.append(int(word))
        if a=="}" and len(word_temp)>=1:
            word="".join(word_temp)#가장 끝 원소가 위 if 문에 안들어가서 중복 작성
            word_temp=[]
            temp.append(int(word))
            depart.append(temp)#최종 단위 temp를 depart로 이동
            temp=[]
    depart.sort(key=len)#원소 길이 오름차순
    for a in depart:
        for b in a:
            if b not in answer:#중복 필터링
                answer.append(b)
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")