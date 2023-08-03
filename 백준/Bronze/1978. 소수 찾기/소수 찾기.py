input()
array = list(map(int, input().split()))

if 1 in array :
    array.remove(1)

count = len(array)

for i in array :
    for k in range(2, i) :
        if i % k == 0 :
            count -= 1
            break



print(count)