array = []
max_ = 0
r = 0
c = 0
for i in range(9) :
    array.append(list(map(int, input().split())))
    for k in range(len(array[i])) :
        if array[i][k] > max_ :
            r, c = i, k
            max_ = array[i][k]

print(max_)
print(r + 1, c + 1)