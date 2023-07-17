import sys

sys.stdin.readline().split()
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
count = 0
answer = []

for i in a :
    if i not in b :
        count += 1
        answer.append(i)

answer.sort()

if count == 0 :
    print(0)
else :
    print(count)
    for i in answer :
        print(i , end = ' ') 

