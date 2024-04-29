def solution(array):
    array_set = set(array)
    counting = []
    
    for i in array_set :
        counting.append(array.count(i))
    
    return -1 if counting.count(max(counting)) >= 2 else max(array, key = array.count)