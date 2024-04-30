def solution(my_string):
    answer = []
    a_upper = [chr(x) for x in range(65, 91)]
    a_lower = [chr(x) for x in range(97, 123)]
    a_all = a_upper + a_lower
    for i in a_all:
        answer.append(my_string.count(i))
            
    return answer