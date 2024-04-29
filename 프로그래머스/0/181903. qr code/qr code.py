def solution(q, r, code):
    answer = ''
    for i in range(0, len(code)):
        if i % q != r:
            continue
        answer += code[i]
            
    return answer