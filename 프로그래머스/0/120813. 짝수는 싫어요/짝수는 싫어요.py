def solution(n):
    result = []
    for i in range(1, n + 1, 2) :
        if i % 2 != 0 :
            result.append(i)
            
    return result