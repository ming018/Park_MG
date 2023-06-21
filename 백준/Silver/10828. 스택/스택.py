import sys

array = []
n = int(sys.stdin.readline())

for _ in range(n) :
    command = sys.stdin.readline().split()

    if command[0] == 'push' :
        array.append(int(command[1]))

    elif command[0] == 'top' :

        if len(array) == 0 :
            print(-1)
            continue

        num2 = array.pop()
        print(num2)
        array.append(num2)
    
    elif command[0] == 'pop' :
        if len(array) == 0 :
            print(-1)
            continue
        print(array.pop())

    elif command[0] == 'size' :
        print(len(array))

    elif command[0] == 'empty' :
        print(1 if len(array) == 0 else 0)
