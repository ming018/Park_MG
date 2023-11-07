
while True :
    array = list(map(int, input().split()))
    array.sort()
    if array[0] == 0 and array[1] == 0 and array[2] == 0 :
        break
    elif array[0] * array[0] + array[1] * array[1] == array[2] * array[2] :
        print('right')
    
    else :
        print('wrong')
    