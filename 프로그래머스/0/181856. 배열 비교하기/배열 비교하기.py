def solution(arr1, arr2):
    # answer = 0
    l1 = len(arr1)
    l2 = len(arr2)
    
    if l1 > l2: 
        return 1
    elif l1 < l2:
        return -1
    else:
        return 1 if sum(arr1) > sum(arr2) else -1 if sum(arr1) < sum(arr2) else 0