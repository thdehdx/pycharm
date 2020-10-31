def solution(skill, skill_trees):
    skill_tree=[]
    skill_list=list(skill)
    answer = 0
    if len(skill_list)==1:
        answer=len(skill_trees)
    else:
        for i in skill_trees:
            skill_tree=list(i)
            level=[len(skill_tree)]*len(skill_list)
            for j in range(len(skill_tree)):
                for k in range(len(skill_list)):
                    if skill_tree[j] == skill_list[k]:
                        level[k]=j
            for a in range(len(level)-1):
                if level[a]>level[a+1]:
                    break
                elif a==len(level)-2:
                    answer+=1
    return answer