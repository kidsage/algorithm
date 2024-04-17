def solution(a, d, included):
    answer = 0
    step = a
    for i in range(0, len(included)):
        if included[i] is True:
            answer += step
        
        step += d
    return answer