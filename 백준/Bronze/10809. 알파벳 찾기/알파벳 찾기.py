array = [-1] * 26
str_ = input()

for i in str_ :
    array[ord(i) - 97] = str_.index(i)

print(*array)