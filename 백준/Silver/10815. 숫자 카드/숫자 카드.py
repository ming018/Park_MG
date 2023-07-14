input()
array = set(map(int, input().split()))
input()
array_check = list(map(int, input().split()))
for i in array_check :
    if i in array :
        print(1, end = ' ')
    else :
        print(0, end = ' ')