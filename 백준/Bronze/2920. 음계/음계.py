array = list(map(int, input().split()))
check = [i for i in range(1, 9)]

if check == array :
    print("ascending")
elif check == list(reversed(array)) :
    print("descending")
else :
    print("mixed")