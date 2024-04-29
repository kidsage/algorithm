def solution(my_string):
    answer = []
    len_string = len(my_string)
    for i in range(0, len_string):
        answer.append(my_string[i:len_string+1])
        
    return sorted(answer)