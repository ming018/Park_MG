array = []
for i in range(2, 10) : 
    if i == 7 or i == 9:
        array.append([i + 1] * 4)
        continue
    array.append([i + 1] * 3)

array = sum(array, [])

str_ = list(input())
sum_ = 0

for i in str_ :
    sum_ += array[ord(i) - 65]

print(sum_)