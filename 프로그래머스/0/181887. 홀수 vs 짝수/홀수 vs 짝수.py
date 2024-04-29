def solution(num_list):
    num1 = 0
    num2 = 0
    sep = 0
    for i in num_list:
        sep += 1
        if sep % 2 == 0:
            num1 += i
        else:
            num2 += i
    
    return max(num1, num2)