def solution(p):
    def divide(w):
        if w == "":  # 조건1번
            return ""
        list_w = list(w)
        cnt = 0
        u = ""
        v = ""
        perfect = True  # w->"올바른 괄호 문자열" 여부#조건3번
        for a in range(len(list_w)):  # 조건2번
            u += list_w[a]
            if list_w[a] == "(":
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:  # 조건3번
                    perfect = False
            if cnt == 0 and a + 1 < len(list_w):  # 분리완료 + 뒤에 더있을 경우
                v = "".join(list_w[a + 1:])
                break
        if perfect:  # 조건3번->u가 올바른 괄호 문자열 인 경우
            u += divide(v)  # 조건3번->v에 대해 1단계부터 다시 수행#조건3-1번
            return u  # 조건 3-1번
        else:  # 조건4번
            temp = "("  # 4-1
            temp += divide(v)  # 4-2
            temp += ")"  # 4-3
            list_temp = list(temp)
            list_u = list(u)
            list_result = list_temp  # 4-4
            for b in range(1, len(list_u) - 1):  # 4-4
                if list_u[b] == "(":
                    list_result.append(")")
                else:
                    list_result.append("(")
            result = "".join(list_result)
            return result

    answer = ''
    answer = divide(p)  # 조건2번

    return answer