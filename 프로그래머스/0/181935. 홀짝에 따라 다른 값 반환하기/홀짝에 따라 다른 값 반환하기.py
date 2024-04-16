def solution(n):
    k = n // 2
    return ((n//2)+1)**2 if n % 2 == 1 else sum([(2*i)**2 for i in range(1, n//2 + 1)])