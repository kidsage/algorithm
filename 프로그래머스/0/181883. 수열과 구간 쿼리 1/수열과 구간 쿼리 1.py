def solution(arr, queries):
    for s, e in queries:
        arr[s:e+1] = list(map(lambda x : x+1, arr[s:e+1]))
    return arr