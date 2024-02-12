import sys

for _ in range(int(sys.stdin.readline())) :
    check = 0
    brackets = sys.stdin.readline()

    for i in brackets :
        if i == '(' :
            check += 1
        elif i == ')' :
            check -= 1

        if check < 0 :
            break

    if check == 0 :
        print('YES')
    else :
        print('NO')