import sys

id = []

for _ in range(int(sys.stdin.readline())) :
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    id.append([age, name])

id.sort(key=lambda x: x[0])

for i in id :
    print(i[0], end = ' ')
    print(i[1])