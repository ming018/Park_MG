array = list(map(int, input().split()))
for i in range(len(array)) :
    array[i] = array[i] ** 2
print(sum(array) % 10)