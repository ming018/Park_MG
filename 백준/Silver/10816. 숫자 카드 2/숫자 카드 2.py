import sys

sys.stdin.readline()
array = list(map(int, sys.stdin.readline().split()))
array_counts = {}

for i in array:
    if i in array_counts:
        array_counts[i] += 1
    else:
        array_counts[i] = 1

sys.stdin.readline()
check_array = list(map(int, sys.stdin.readline().split()))

for i in check_array:
    if i not in array_counts:
        print(0, end=' ')
    else:
        print(array_counts[i], end=' ')
