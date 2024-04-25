import re

def solution(l, r):
    pattern = r'^(?=.*[05])(?!.*[^05])[\d]+$'
    answer = [num for num in range(l, r+1) if re.match(pattern, str(num))]
    
    if not answer:
        answer.append(-1)
        
    return answer