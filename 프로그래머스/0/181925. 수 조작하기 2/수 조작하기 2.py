def solution(numLog):
    answer = ''
    prenum = True
    for i in numLog:
        if prenum is True:
            prenum = i
            continue
        
        if i - prenum == 1:
            answer += 'w'
        elif i - prenum == 10:
            answer += 'd'
        elif i - prenum == -1:
            answer += 's'
        else:
            answer += 'a'
        prenum = i
        
    return answer