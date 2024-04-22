def solution(arr, queries):
    answer = []
    for element in queries:
        a = -1
        for i in range(element[0], element[1]+1):
            if arr[i] > element[2]:
                if a == -1 or a > arr[i]:
                    a = arr[i]
        answer.append(a)
    return answer