limit = int(input())
for i in range(limit) :
    for _ in range(i) :
        print(' ', end = '')

    for _ in range(limit - i) :
        print('*', end = '')
    
    print()