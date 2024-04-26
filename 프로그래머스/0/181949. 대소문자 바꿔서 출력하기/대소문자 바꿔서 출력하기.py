strs = list(input())

for i in strs :
    if i.isupper() :
        print(i.lower(), end = '')
    if i.islower() :
        print(i.upper(), end = '')