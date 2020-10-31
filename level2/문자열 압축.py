def solution(s):
    s_list=list(s)
    answer_list=[]
    answer = len(s_list)
    total=0
    for i in range(1,int(len(s_list)/2)+1):
        word=""
        s_word=[]
        for j in s_list:
            word+=j
            if len(word)==i:
                s_word.append(word)
                word=""
        answer_list=[]
        for k in range(len(s_word)):
            if k==0:
                stadard=s_word[k]
                cnt=1
            elif k==len(s_word)-1:
                if stadard==s_word[k]:
                    cnt+=1
                    answer_list.append(str(cnt))
                    answer_list.append(stadard)
                    total += cnt
                else:
                    answer_list.append(str(cnt))
                    answer_list.append(stadard)
                    answer_list.append(s_word[k])
                    cnt+=1
                    total += cnt
            else:
                if stadard==s_word[k]:
                    cnt+=1
                else:
                    answer_list.append(str(cnt))
                    answer_list.append(stadard)
                    total+=cnt
                    stadard=s_word[k]
                    cnt=1
        total=total*i
        for j in range(len(answer_list)):
            if answer_list[j] == "1":
                answer_list[j]=""
        for j in range(total,len(s_list)):
            answer_list.append(s_list[j])
        answer_str="".join(answer_list)
        if answer>len(answer_str):
            answer=len(answer_str)
        total=0
    return answer


print(solution("xxxxxxxxxxyyy"))