for _ in range(int(input())) :
    check = 0
    brackets = input()

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