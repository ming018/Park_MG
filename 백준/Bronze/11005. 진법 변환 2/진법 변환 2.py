import sys

num, jinbob = map(int, sys.stdin.readline().split())
change = {}
for i in range(jinbob - 10) :
    change[i + 10] = chr(i + 65)
changed = ''

while(num != 0) :
    if num % jinbob >= 10 :
        changed += change[num % jinbob]
    else :
        changed += str(num % jinbob)
    num = num // jinbob

print(changed[::-1])