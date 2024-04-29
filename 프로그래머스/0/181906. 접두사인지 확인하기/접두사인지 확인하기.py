def solution(my_string, is_prefix):
    list_prefix = [my_string[0:i+1] for i in range(1, len(my_string))]
    return 1 if is_prefix in list_prefix else 0