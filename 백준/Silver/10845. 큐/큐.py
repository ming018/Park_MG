import sys

array = []
for _ in range(int(sys.stdin.readline())) :
    com = list(map(str, sys.stdin.readline().split()))

    if com[0] == 'push' :
        array.append(int(com[1]))

    elif com[0] == 'pop' :
        if len(array) == 0 :
            print(-1)
            continue
        print(array.pop(0))

    elif com[0] == 'empty' :
        if len(array) == 0 :
            print(1)
        else :
            print(0)

    elif com[0] == 'size' :
        print(len(array))

    elif com[0] == 'front' :
        if len(array) == 0 :
            print(-1)
        else :
            num = array.pop(0)
            print(num)
            array.insert(0, num)
            
    elif com[0] == 'back' :
        if len(array) == 0 :
            print(-1)
        else :
            num = array.pop()
            print(num)
            array.append(num)