str_ = list(input().upper())
str_set = set(str_)
array = []

for i in str_set :
    array.append([str_.count(i), i])

array_count = list(array[i][0] for i in range(len(array)))
array = sum(array, [])

print("?" if array_count.count(max(array_count)) >= 2 else array[array.index(max(array_count)) + 1])