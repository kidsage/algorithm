def solution(arr, n):
    
    if len(arr) % 2 == 1:
        for i in range(0, len(arr)):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i in range(0, len(arr)):
            if i % 2 == 1:
                arr[i] += n

    return arr