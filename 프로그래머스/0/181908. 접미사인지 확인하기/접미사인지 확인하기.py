def solution(my_string, is_suffix):
    list_end = [my_string[i:len(my_string)+1] for i in range(0, len(my_string))]
    return 1 if is_suffix in list_end else 0