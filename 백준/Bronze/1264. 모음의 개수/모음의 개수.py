moum = ('a', 'e', 'i', 'o', 'u')

string = input()
while True :
    if string == "#" :
        break
    string = string.lower()
    num = 0
    for i in string :
        if i in moum :
            num += 1
    print(num)

    string = input()