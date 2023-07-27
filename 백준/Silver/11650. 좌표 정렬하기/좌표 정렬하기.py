import sys

array = []

for _ in range(int(sys.stdin.readline())) :
    array.append(list(map(int, sys.stdin.readline().split())))

array.sort()
for i in range(len(array)) :
    print(array[i][0], end = ' ')
    print(array[i][1])