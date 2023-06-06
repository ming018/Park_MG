str_ = (input().upper())
array = list(set(str_))
count_ = []

for i in array :
    count_.append(str_.count(i))

print("?" if count_.count(max(count_)) >= 2 else array[count_.index(max(count_))])