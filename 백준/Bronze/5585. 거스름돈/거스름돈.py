import sys
count = 0

pay = 1000 - int(sys.stdin.readline())

count += pay // 500
pay = pay % 500

count += pay // 100
pay = pay % 100

count += pay // 50
pay = pay % 50

count += pay // 10
pay = pay % 10

count += pay // 5
pay = pay % 5

count += pay // 1
pay = pay % 1

print(count)