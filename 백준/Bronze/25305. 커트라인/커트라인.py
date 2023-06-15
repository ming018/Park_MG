limit, target = map(int, input().split())
array = []
array = list(map(int, input().split()))

array.sort(reverse = 1)

print(array[target - 1])