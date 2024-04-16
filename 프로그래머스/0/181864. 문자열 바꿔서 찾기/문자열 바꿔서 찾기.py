def solution(myString, pat):
    
    result = ''
    for i in myString:
        if i == 'A':
            result += 'B'
        else:
            result += 'A'
    
    if pat in result:
        return 1
    
    return 0