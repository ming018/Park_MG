import sys

array = []
for i in range(int(input())) :
    array.append(int(sys.stdin.readline()))

array.sort()

for i in array :
    print(i)