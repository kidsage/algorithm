def solution(num_list):
    mtp = 1
    for i in num_list:
        mtp *= i
    return 1 if sum(num_list)**2 > mtp else 0