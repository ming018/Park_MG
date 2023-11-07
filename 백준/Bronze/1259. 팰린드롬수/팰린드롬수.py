while True :
    string = input()

    if string == '0' :
        break

    count = 0
    for i in range(len(string) // 2) :
        if string[i] != string[len(string) - (i + 1) ] :
            break
        count += 1
    if count == len(string) // 2 :
        print("yes")
    else :
        print("no")