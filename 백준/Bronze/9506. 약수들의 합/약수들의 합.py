
while True :
    num = int(input())
    if num == -1 :
        break

    array = []
    for i in range(1, num) :
        if num % i == 0 :
            array.append(i)
    
    if sum(array) == num :
        print(num, end = ' = ')
        for i in range(1, (len(array) + (len(array) - 1)), 2) :
            array.insert(i, '+')
        
        for i in array :
            print(i, end = ' ')

        print()
        
    else :
        print(num, 'is NOT perfect.')