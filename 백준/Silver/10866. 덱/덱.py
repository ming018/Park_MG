import sys

array = []

for _ in range(int(input())) : 
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == 'push_front' :
        array.insert(0, int(command[1]))
    
    elif command[0] == 'push_back' :
        array.append(int(command[1]))

    elif command[0] == 'pop_front' :
        if len(array) == 0 :
            print(-1)
            continue
        num = array.pop(0)
        print(num)
        
    elif command[0] == 'pop_back' :
        if len(array) == 0 :
            print(-1)
            continue
        num = array.pop()
        print(num)
    
    elif command[0] == 'size' :
        print(len(array))
    
    elif command[0] == 'empty' :
        if len(array) == 0 :
            print(1)
        else :
            print(0)
    
    elif command[0] == 'front' :
        if len(array) == 0 :
            print(-1)
            continue
        print(array[0])

    elif command[0] == 'back' :
        if len(array) == 0 :
            print(-1)
            continue
        print(array[-1])