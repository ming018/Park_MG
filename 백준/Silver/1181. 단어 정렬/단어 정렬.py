strs = []

for _ in range(int(input())) :
    strs.append(input())
strs = list(set(strs))
strs.sort()
strs.sort(key = len)

for i in strs :
    print(i)