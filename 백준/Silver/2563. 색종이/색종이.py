import sys

array = [[0] * 100 for _ in range(100)]
area = 0

for _ in range(int(sys.stdin.readline())) :
    x, y = map(int, sys.stdin.readline().split())
    for i in range(y, y + 10) :
        array[i][x : x + 10] = [1] * 10

for i in range(len(array)) :
    area += array[i].count(1)

print(area)