count = int(input())
array = list(map(int, input().split()))
max_score = max(array)

for i in range(count) :
    array[i] = (array[i] / max_score) * 100

print(sum(array) / count)