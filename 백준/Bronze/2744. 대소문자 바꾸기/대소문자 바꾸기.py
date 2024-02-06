msg = input()

for i in msg :
    if i.islower() :
        print(i.upper(), end = '')
    else :
        print(i.lower(), end='')
print()
