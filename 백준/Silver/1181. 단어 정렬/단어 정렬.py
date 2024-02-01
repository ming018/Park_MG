import sys

strs = []

for _ in range(int(sys.stdin.readline())) :
    strs.append(sys.stdin.readline().strip())
strs = list(set(strs))
strs.sort()
strs.sort(key = len)

for i in strs :
    print(i)