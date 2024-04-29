def solution(num_list):
    result = 0
    if len(num_list) > 10:
        for i in num_list:
            result += i
    else:
        result = 1
        for i in num_list:
            result = result * i
        
    return result