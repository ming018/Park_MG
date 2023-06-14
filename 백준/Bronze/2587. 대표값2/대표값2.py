array = []
for _ in range(5) :
    array.append(int(input()))

array.sort()
print(int(sum(array)/len(array)))
print(array[len(array)//2])