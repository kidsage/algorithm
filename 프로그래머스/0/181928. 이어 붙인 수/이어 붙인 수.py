def solution(num_list):
    a1 = ''
    a2 = ''
    for i in num_list:
        if i % 2 == 0:
            a2 += str(i)
        else:
            a1 += str(i)
    
    return int(a1)+int(a2)