def solution(arr):
    index_list = []
    for i in range(0, len(arr)):
        if arr[i] == 2:
            index_list.append(i)
    return arr[index_list[0]:index_list[-1]+1] if index_list else [-1]