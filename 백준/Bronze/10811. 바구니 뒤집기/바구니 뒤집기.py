len, count = map(int, input().split())
array = [(i + 1) for i in range(len)]

for i in range(count) :
    i, j = map(int,input().split())
    array[i - 1 : j] = array[j - 1 : i - 2 if i > 1 else None : -1]

print(" ".join(str(i) for i in array))