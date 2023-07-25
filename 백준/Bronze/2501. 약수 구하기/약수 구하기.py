import sys
num1, num2 = map(int, sys.stdin.readline().split())

array = []

for i in range(1, num1 + 1) :
    if num1 % i == 0 :
        array.append(i)

if len(array) < num2 :
    print(0)
else :
    print(array[num2 - 1])