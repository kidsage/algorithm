def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        int_i = int(i[s:s+l])
        if int_i > k:
            answer.append(int_i)
    return answer