apart = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15) :
    apart[i][0] = 1
    apart[0][i] = i + 1

for i in range(1, 15) :
    for k in range(1, 15) :
        apart[i][k] = sum(apart[i - 1][0 : k + 1])

count = int(input())
str_ = ""
for _ in range(count) :
    floor = int(input())
    num = int(input())
    print(apart[floor][num - 1])