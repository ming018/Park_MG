n, m = map(int, input().split())
array = []
array_ = []

for i in range(n) :
    array.append(list(map(int, input().split())))

for i in range(n) :
    array_.append(list(map(int, input().split())))

for i in range(n) :
    for k in range(m) :
        print(array[i][k] + array_[i][k], end = ' ')
    print()